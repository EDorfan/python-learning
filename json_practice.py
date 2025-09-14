import json
from typing import Any, Dict, List


def load_people_from_string(people_json: str) -> Dict[str, Any]:
	"""Parse a JSON string and return a Python dict.

	Expected top-level shape: {"people": [ {"name": str, "phone": str, "emails": [str, ...], "has_license": bool}, ... ]}
	"""
	# TODO: implement using json.loads
	raise NotImplementedError


def remove_key_from_people(data: Dict[str, Any], key_to_remove: str) -> Dict[str, Any]:
	"""Return a new dict where each person dict no longer contains key_to_remove.

	Do not mutate the input dict; return a deep-copied/constructed result.
	"""
	# TODO: implement without mutating input
	raise NotImplementedError


def people_to_sorted_json(data: Dict[str, Any]) -> str:
	"""Return a JSON string with sorted keys and 2-space indentation.

	Use json.dumps with indent=2 and sort_keys=True.
	"""
	# TODO: implement dumps formatting
	raise NotImplementedError


def get_people_without_license(data: Dict[str, Any]) -> List[Dict[str, Any]]:
	"""Return people whose has_license is False."""
	# TODO: filter by has_license flag
	raise NotImplementedError


def extract_emails(data: Dict[str, Any]) -> List[str]:
	"""Flatten and return all email addresses from the people list (preserve order)."""
	# TODO: gather emails from each person in order
	raise NotImplementedError


def save_json_to_file(data: Dict[str, Any], path: str) -> None:
	"""Write dict to a file as JSON (UTF-8), sorted keys and pretty-printed."""
	# TODO: open(path, 'w', encoding='utf-8') and json.dump(...)
	raise NotImplementedError


def load_json_from_file(path: str) -> Dict[str, Any]:
	"""Load dict from a JSON file (UTF-8)."""
	# TODO: open(path, 'r', encoding='utf-8') and json.load(...)
	raise NotImplementedError


EXAMPLE_PEOPLE_JSON = (
	"""
	{
	  "people": [
	    {
	      "name": "John Smith",
	      "phone": "615-555-7164",
	      "emails": ["john.doe@example.com", "john@doe.com"],
	      "has_license": false
	    },
	    {
	      "name": "Jane Doe",
	      "phone": "615-555-7165",
	      "emails": ["jane.doe@example.com", "jane@doe.com"],
	      "has_license": true
	    }
	  ]
	}
	"""
).strip()


ADDENDUM = (
	"""
	Essential JSON/Python skills not to miss:
	- json.loads vs json.load: loads parses a string; load reads from a file-like object.
	- json.dumps vs json.dump: dumps returns a string; dump writes to a file-like object.
	- Booleans are lowercase in JSON (true/false) but capitalized in Python (True/False). The json module maps them automatically.
	- Ensure files are opened with explicit encoding="utf-8" for portability.
	- Avoid mutating inputs in helper functions unless required; prefer returning new objects.
	- Use indent and sort_keys for deterministic output when testing.
	- When reading unknown JSON, validate shape defensively: use dict.get with defaults or try/except KeyError.
	"""
).strip()