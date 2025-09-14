from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Union
import json


def parse_json_string(json_string: str) -> Dict[str, Any]:
    return json.loads(json_string)


def get_people_list(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return list(data.get("people", []))


def get_person_names(data: Dict[str, Any]) -> List[str]:
    return [person.get("name", "") for person in get_people_list(data)]


def remove_field_from_people(data: Dict[str, Any], field_name: str) -> Dict[str, Any]:
    for person in get_people_list(data):
        person.pop(field_name, None)
    return data


def filter_people_by_license(data: Dict[str, Any], has_license: bool) -> List[Dict[str, Any]]:
    return [p for p in get_people_list(data) if bool(p.get("has_license")) is has_license]


def stringify_json(data: Any, indent: int = 2, sort_keys: bool = True) -> str:
    return json.dumps(data, indent=indent, sort_keys=sort_keys, ensure_ascii=False)


def load_json_file(path: Union[str, Path]) -> Any:
    with open(Path(path), "r", encoding="utf-8") as f:
        return json.load(f)


def save_json_file(path: Union[str, Path], data: Any, ensure_ascii: bool = False) -> None:
    with open(Path(path), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True, ensure_ascii=ensure_ascii)

