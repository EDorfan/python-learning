### Practice Packs: Naming and Testing

- **Practice file**: `<topic>_practice.py`
- **Solutions file**: `<topic>_solutions.py`
- **Tests**: `tests/test_<topic>_practice.py`
- **Fixtures/data**: `fixtures/`

### How to run the tests

1. Install pytest (once):
```bash
pip install pytest
```
2. Run tests:
```bash
pytest -q
```

### How to use

- Open the `<topic>_practice.py` file and implement the `NotImplementedError` functions.
- Use the docstrings and examples as guidance. The tests describe the expected behavior.
- Compare with `<topic>_solutions.py` after you try.

### Requesting new topics

Tell me the topic names (e.g., `Decorators`, `Property_Decorators`, `Special_Methods`). I will generate a matching pack with the same structure and ready-to-run tests.

### JSON pack extras (addendum)

- Custom decode: `json.loads(s, object_hook=...)`, `parse_float=Decimal`
- Custom encode: subclass `json.JSONEncoder` or pass `default=`
- Unicode vs ASCII: `ensure_ascii=False` for UTF-8
- Errors: catch `json.JSONDecodeError` with a helpful message
- Large files: consider streaming (e.g., `ijson`) or JSONL

