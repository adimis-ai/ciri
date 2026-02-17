# Contributing Checklist

Before opening a PR:

1. Create a feature branch from main:

```bash
git checkout -b feature/your-feature
```

2. Run linters and formatters:

```bash
ruff check src/ --fix
black src/
mypy src/
```

3. Run tests:

```bash
pytest
```

4. Update documentation if needed (README, CONTRIBUTING, or SKILL.md files).

5. Commit with clear messages and push your branch.

PR template guidance

- Describe the change, why it's needed, and how to test it.
- Link relevant issues.
- Ensure CI (if present) passes.
