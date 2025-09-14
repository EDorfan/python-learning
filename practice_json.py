"""
Practice Module: JSON

Standard naming: practice_<topic>.py → this file is `practice_json.py`.

Complete the functions below to practice core JSON skills in Python. Each
function has a focused learning goal and is covered by tests in
`tests/test_practice_json.py`.

Run tests:
  - pip install -r requirements.txt
  - pytest -q

Notes:
  - Do not change function names or signatures; tests rely on them.
  - Prefer returning new data structures over mutating inputs, unless stated.

Addendum: Essential JSON skills
  - json.loads/json.dumps basic usage and parameters (indent, sort_keys, ensure_ascii)
  - Robust error handling: catch json.JSONDecodeError and surface helpful errors
  - Loading from files with json.load and proper file handling
  - Avoiding unintended mutation: use deep copies when removing/modifying fields
  - Hooks: parse_float/parse_int/object_pairs_hook for advanced parsing
  - Custom encoding: default= to convert unsupported types (e.g., dataclasses)
  - Security: never load untrusted JSON as code; JSON is data, not Python
"""

from __future__ import annotations

import copy
import json
from typing import Any, Dict, List


def load_json_string(json_str: str) -> Dict[str, Any]:
    """Parse a JSON string into a Python object (dict-based top level).

    Learning focus:
      - json.loads
      - Error handling (map JSONDecodeError → ValueError with context)

    Example:
        >>> load_json_string('{"a": 1}')
        {'a': 1}

    Raises:
        ValueError: if the input is not valid JSON or the top-level is not an object.
    """
    raise NotImplementedError


def get_people_names(data: Dict[str, Any]) -> List[str]:
    """Return a list of names from data shaped like:

        {
          "people": [{"name": "John", ...}, {"name": "Jane", ...}]
        }

    Learning focus:
      - Navigating nested structures
      - List comprehensions

    Example:
        >>> get_people_names({"people": [{"name": "Ann"}, {"name": "Bob"}]})
        ['Ann', 'Bob']
    """
    raise NotImplementedError


def remove_field_from_people(data: Dict[str, Any], field_name: str) -> Dict[str, Any]:
    """Return a new copy of data with `field_name` removed from each person.

    The original input must NOT be mutated.

    Learning focus:
      - Deep copying nested structures
      - Safe deletion with dict operations

    Example:
        >>> d = {"people": [{"name": "Ann", "phone": "123"}]}
        >>> out = remove_field_from_people(d, "phone")
        >>> out
        {'people': [{'name': 'Ann'}]}
        >>> d  # original unchanged
        {'people': [{'name': 'Ann', 'phone': '123'}]}
    """
    raise NotImplementedError


def dump_json_pretty(data: Dict[str, Any]) -> str:
    """Serialize `data` to a pretty JSON string.

    Requirements:
      - indent=2
      - sort_keys=True
      - ensure_ascii=False (preserve unicode where possible)

    Learning focus:
      - json.dumps options and readability

    Example:
        >>> dump_json_pretty({"b": 1, "a": 2}).splitlines()[0]
        '{'
    """
    raise NotImplementedError


def load_json_file(path: str) -> Dict[str, Any]:
    """Load JSON data from a file path.

    Learning focus:
      - json.load with context manager
      - Basic I/O hygiene

    Example:
        >>> # see tests for file-based example
        >>> isinstance(load_json_file('tests/fixtures/states.json'), dict)
        True
    """
    raise NotImplementedError


def validate_people_schema(data: Dict[str, Any]) -> bool:
    """Validate that `data` has the expected people schema.

    Expected shape:
      - dict with key "people"
      - value is a list of dicts
      - each person has keys: "name" (str), "emails" (list), "has_license" (bool)

    Return True if valid, otherwise False.

    Learning focus:
      - Defensive checks and types at runtime
      - Practical schema validation without external libs
    """
    raise NotImplementedError

