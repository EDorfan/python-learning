import json
from pathlib import Path

import pytest

import practice_json as pj


def test_load_json_string_success():
    data = pj.load_json_string('{"people": []}')
    assert isinstance(data, dict)
    assert data["people"] == []


@pytest.mark.parametrize("bad", [
    "", "not json", "[]", "123", "null"
])
def test_load_json_string_errors(bad):
    with pytest.raises(ValueError):
        pj.load_json_string(bad)


def test_get_people_names():
    data = {"people": [{"name": "John"}, {"name": "Jane"}]}
    assert pj.get_people_names(data) == ["John", "Jane"]


def test_remove_field_from_people_does_not_mutate_input():
    original = {"people": [{"name": "Ann", "phone": "123"}]}
    result = pj.remove_field_from_people(original, "phone")

    # original unchanged
    assert original == {"people": [{"name": "Ann", "phone": "123"}]}

    # field removed in result
    assert result == {"people": [{"name": "Ann"}]}


def test_dump_json_pretty_options():
    data = {"b": 1, "a": 2, "u": "✓"}
    s = pj.dump_json_pretty(data)
    # pretty format checks
    assert s.splitlines()[0] == "{"
    # keys sorted: a before b
    assert s.index('\n  "a"') < s.index('\n  "b"')
    # unicode preserved
    assert "✓" in s


def test_load_json_file(tmp_path: Path):
    content = {"people": [{"name": "John", "emails": [], "has_license": True}]}
    p = tmp_path / "sample.json"
    p.write_text(json.dumps(content))
    loaded = pj.load_json_file(str(p))
    assert loaded == content


@pytest.mark.parametrize(
    "data, expected",
    [
        ({"people": [{"name": "A", "emails": [], "has_license": True}]}, True),
        ({"people": []}, True),
        ({}, False),
        ({"people": [{}]}, False),
        ({"people": [{"name": 1, "emails": [], "has_license": True}]}, False),
        ({"people": [{"name": "A", "emails": "not list", "has_license": True}]}, False),
        ({"people": [{"name": "A", "emails": [], "has_license": "yes"}]}, False),
    ],
)
def test_validate_people_schema(data, expected):
    assert pj.validate_people_schema(data) is expected

