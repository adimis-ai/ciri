# Test & Lint

Test framework

- Uses pytest (dev dependency in pyproject.toml).
- Test directory: tests/

Run tests

```bash
# Run all tests
pytest

# With verbose output
pytest -v

# Run a single file
pytest tests/test_somefile.py
```

Lint & format

- Ruff for linting, Black for formatting, MyPy for types (all listed in optional dev dependencies).

Commands

```bash
# Check formatting
black --check src/
# Apply formatting
black src/

# Lint (ruff)
ruff check src/ --fix

# Type checking
mypy src/
```

Notes

- CONTRIBUTING.md includes a pre-PR checklist recommending running ruff/black and pytest before creating a PR.
- Ensure you run these inside the uv-managed environment (`uv sync --dev` then `uv pip install -e .`).
