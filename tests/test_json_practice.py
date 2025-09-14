from __future__ import annotations

from pathlib import Path
import json
import importlib

import pytest


# Import the practice module under test
practice = importlib.import_module("json_practice")


FIXTURES_DIR = Path(__file__).resolve().parents[1] / "fixtures"


@pytest.fixture()
def people_data_from_example() -> dict:
    return practice.parse_json_string(practice.EXAMPLE_PEOPLE_JSON)


@pytest.fixture()
def people_data_from_file() -> dict:
    path = FIXTURES_DIR / "people.json"
    return practice.load_json_file(path)


def test_parse_json_string_and_names(people_data_from_example: dict) -> None:
    assert isinstance(people_data_from_example, dict)
    names = practice.get_person_names(people_data_from_example)
    assert names == ["John Smith", "Jane Doe"]


def test_get_people_and_remove_field(people_data_from_example: dict) -> None:
    people = practice.get_people_list(people_data_from_example)
    assert isinstance(people, list) and len(people) == 2

    # Remove phones and verify removal doesn't raise and is in-place
    practice.remove_field_from_people(people_data_from_example, "phone")
    assert all("phone" not in p for p in people_data_from_example["people"])  # type: ignore[index]


def test_stringify_and_parse_roundtrip(people_data_from_example: dict) -> None:
    practice.remove_field_from_people(people_data_from_example, "phone")
    s = practice.stringify_json(people_data_from_example, indent=2, sort_keys=True)
    reparsed = json.loads(s)
    assert reparsed == people_data_from_example


def test_load_and_save_json_roundtrip(tmp_path: Path, people_data_from_file: dict) -> None:
    out_path = tmp_path / "out.json"
    practice.save_json_file(out_path, people_data_from_file)
    loaded = practice.load_json_file(out_path)
    assert loaded == people_data_from_file


def test_filter_people_by_license(people_data_from_file: dict) -> None:
    licensed = practice.filter_people_by_license(people_data_from_file, True)
    unlicensed = practice.filter_people_by_license(people_data_from_file, False)
    assert [p["name"] for p in licensed] == ["Jane Doe"]
    assert [p["name"] for p in unlicensed] == ["John Smith"]


def test_names_from_file_fixture(people_data_from_file: dict) -> None:
    assert practice.get_person_names(people_data_from_file) == ["John Smith", "Jane Doe"]

