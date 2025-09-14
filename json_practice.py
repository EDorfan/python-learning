"""
JSON Practice Exercises

Implement the functions below to practice common JSON tasks in Python.

Conventions
- Keep function signatures unchanged.
- Do not change global constants.
- Aim for clear, readable code.

Examples
>>> data = parse_json_string(EXAMPLE_PEOPLE_JSON)
>>> get_person_names(data)
['John Smith', 'Jane Doe']
>>> remove_field_from_people(data, 'phone')
>>> 'phone' in data['people'][0]
False

Addendum: Essential JSON skills to know
- Custom decoding using object_hook (e.g., transform dicts while loading)
- Custom encoding via JSONEncoder/ default for non-serializable objects (datetime, Decimal)
- parse_float / parse_int parameters (e.g., load Decimals precisely)
- ensure_ascii vs UTF-8 output; newline and indent controls
- Robust error handling: json.JSONDecodeError
- Streaming/iterative parsing for large files (e.g., ijson) and newline-delimited JSON (JSONL)
- Dataclass/Typed model conversions (dataclasses.asdict / pydantic BaseModel.json)
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Union
import json


# Example JSON used across exercises
EXAMPLE_PEOPLE_JSON = (
    '{\n'
    '    "people": [\n'
    '        {\n'
    '            "name": "John Smith",\n'
    '            "phone": "615-555-7164",\n'
    '            "emails": ["john.doe@example.com", "john@doe.com"],\n'
    '            "has_license": false\n'
    '        },\n'
    '        {\n'
    '            "name": "Jane Doe",\n'
    '            "phone": "615-555-7165",\n'
    '            "emails": ["jane.doe@example.com", "jane@doe.com"],\n'
    '            "has_license": true\n'
    '        }\n'
    '    ]\n'
    '}\n'
)


def parse_json_string(json_string: str) -> Dict[str, Any]:
    """Parse a JSON string and return a Python object (dict/list/etc.).

    Return type should match the top-level JSON structure.
    """
    raise NotImplementedError


def get_people_list(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Return the list under the 'people' key from parsed data."""
    raise NotImplementedError


def get_person_names(data: Dict[str, Any]) -> List[str]:
    """Return a list of names from the people list, preserving order."""
    raise NotImplementedError


def remove_field_from_people(data: Dict[str, Any], field_name: str) -> Dict[str, Any]:
    """Remove a field from each person dict in-place (if present) and return data.

    Should not raise if the field is missing in a person.
    """
    raise NotImplementedError


def filter_people_by_license(data: Dict[str, Any], has_license: bool) -> List[Dict[str, Any]]:
    """Return a list of people filtered by their 'has_license' boolean value."""
    raise NotImplementedError


def stringify_json(data: Any, indent: int = 2, sort_keys: bool = True) -> str:
    """Serialize a Python object to a JSON string with indent and sorted keys by default."""
    raise NotImplementedError


def load_json_file(path: Union[str, Path]) -> Any:
    """Load JSON from a UTF-8 encoded file and return the resulting Python object."""
    raise NotImplementedError


def save_json_file(path: Union[str, Path], data: Any, ensure_ascii: bool = False) -> None:
    """Save a Python object as JSON to a UTF-8 encoded file.

    By default, writes UTF-8 (ensure_ascii=False) to preserve non-ASCII characters.
    """
    raise NotImplementedError


if __name__ == "__main__":
    # Mini demo
    parsed = parse_json_string(EXAMPLE_PEOPLE_JSON)
    print(get_person_names(parsed))
    remove_field_from_people(parsed, "phone")
    print(stringify_json(parsed))

