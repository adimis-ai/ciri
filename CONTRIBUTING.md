# Contributing to CIRI

Thank you for your interest in contributing to CIRI! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Code Style](#code-style)
- [Testing](#testing)

---

## Code of Conduct

By participating in this project, you agree to maintain a welcoming and inclusive environment. Be respectful and constructive in all interactions.

---

## How to Contribute

### Reporting Bugs

1. **Search existing issues** to avoid duplicates
2. **Open a new issue** with:
   - A clear, descriptive title
   - Steps to reproduce the bug
   - Expected vs. actual behavior
   - Your environment (OS, Python version, CIRI version)
   - Error messages or logs (if applicable)

### Suggesting Features

1. **Search existing issues** to see if it's been suggested
2. **Open a new issue** with:
   - A clear description of the feature
   - Why it would be useful
   - Possible implementation approach (optional)

### Contributing Code

1. Fork the repository
2. Create a feature branch from `main`
3. Make your changes
4. Submit a pull request

---

## Development Setup

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- Git

### Setup Steps

```bash
# Clone your fork
git clone git@github.com:YOUR_USERNAME/ciri.git
cd ciri

# Install dependencies (including dev dependencies)
uv sync --dev

# Install in editable mode
uv pip install -e .

# Verify installation
ciri --help
```

---

## Pull Request Process

### Before Submitting

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make focused commits** with clear messages

3. **Run linting**:
   ```bash
   ruff check src/
   black --check src/
   ```

4. **Run tests**:
   ```bash
   pytest
   ```

5. **Update documentation** if needed

### Submitting

1. Push your branch to your fork
2. Open a Pull Request against `main`
3. Fill out the PR template with:
   - Description of changes
   - Related issue (if applicable)
   - Screenshots (for UI changes)
   - Testing done

### Review Process

- Maintainers will review your PR
- Address any requested changes
- Once approved, your PR will be merged

---

## Code Style

We use the following tools to maintain code quality:

| Tool | Purpose |
|------|---------|
| **Black** | Code formatting |
| **Ruff** | Linting |
| **MyPy** | Static type checking |

### Running Code Quality Tools

```bash
# Format code
black src/

# Run linter
ruff check src/ --fix

# Type checking
mypy src/
```

### Guidelines

- Use type hints for function parameters and return values
- Keep functions focused and under 50 lines when possible
- Write docstrings for public functions and classes
- Follow PEP 8 conventions

---

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_specific.py

# Run with verbose output
pytest -v
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files with `test_` prefix
- Use descriptive test function names
- Test edge cases and error conditions

---

## Questions?

Open an issue or reach out to the maintainers for help.

---

Thank you for contributing! 🎉
