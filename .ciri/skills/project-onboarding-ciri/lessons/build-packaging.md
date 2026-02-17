# Build & Packaging

Packaging
- Project uses hatchling (pyproject.toml -> [build-system] requires = ["hatchling"]).
- Wheel target configured: tool.hatch.build.targets.wheel -> packages = ["src"]

Build commands

- Build a wheel (isolated):

```bash
python -m build --wheel
# or using hatch
hatch build -t wheel
```

- Install wheel locally:

```bash
pip install dist/ciri_copilot-0.1.0-py3-none-any.whl
```

PyInstaller (standalone binary)

- The repository includes build.py which wraps PyInstaller to create a single-file binary and copy it to src-tauri/binaries.
- Typical usage:

```bash
python build.py --target x86_64-unknown-linux-gnu
```

- build.py adds many hidden imports and uses `--collect-all` for several large packages (langchain, langgraph, pydantic, playwright).

Notes

- The build.py script expects PyInstaller available (dev dependency). For reproducible builds use `uv sync --dev` and run inside the uv-managed environment.
- Tauri integration: build.py copies final binary to `src-tauri/binaries/` for use by a Tauri sidecar (if present).
