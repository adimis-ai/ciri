import pytest
import asyncio
from pathlib import Path
from unittest.mock import MagicMock, patch, AsyncMock
from src.middlewares.tookits import ToolkitInjectorMiddleware


@pytest.fixture
def project_root(tmp_path):
    """Create a mock project structure with a toolkit."""
    ciri_dir = tmp_path / ".ciri"
    toolkits_dir = ciri_dir / "toolkits"
    tk_dir = toolkits_dir / "test_toolkit"
    src_dir = tk_dir / "src"

    toolkits_dir.mkdir(parents=True)
    src_dir.mkdir(parents=True)

    (tk_dir / "pyproject.toml").write_text("""
[project]
name = "test_toolkit"
version = "0.1.0"
dependencies = ["fastmcp"]
""")
    (src_dir / "main.py").write_text("print('hello')")

    return tmp_path


class MockTool:
    def __init__(self, name):
        self.name = name


class MockRequest:
    def __init__(self, tools=None):
        self.tools = tools or []


@pytest.mark.asyncio
async def test_toolkit_discovery_and_injection(project_root):
    # Mock subprocess.run to avoid actual uv sync
    # Mock MultiServerMCPClient to avoid actual MCP server startup
    with (
        patch("subprocess.run") as mock_run,
        patch("src.middlewares.tookits.MultiServerMCPClient") as mock_client_class,
    ):

        # Setup mock client
        mock_client = MagicMock()
        mock_client.get_tools = AsyncMock(
            return_value=[MockTool("echo"), MockTool("add")]
        )
        mock_client_class.return_value = mock_client

        # Initialize middleware
        middleware = ToolkitInjectorMiddleware(scan_root=project_root)

        # Verify discovery
        assert len(middleware._toolkit_versions) == 1
        assert (
            str(project_root / ".ciri" / "toolkits" / "test_toolkit")
            in middleware._toolkit_versions
        )

        # Verify sync was called
        mock_run.assert_called_once()
        assert mock_run.call_args[0][0] == ["uv", "sync"]

        # Verify tools are fetched
        # Give some time for the background task to complete
        for _ in range(10):
            if middleware.tools:
                break
            await asyncio.sleep(0.1)

        assert len(middleware.tools) == 2
        assert {t.name for t in middleware.tools} == {"echo", "add"}

        # Test injection
        request = MockRequest(tools=[MockTool("existing_tool")])
        middleware._inject_tools(request)

        assert len(request.tools) == 3
        assert {t.name for t in request.tools} == {"existing_tool", "echo", "add"}


@pytest.mark.asyncio
async def test_toolkit_version_change(project_root):
    with (
        patch("subprocess.run") as mock_run,
        patch("src.middlewares.tookits.MultiServerMCPClient") as mock_client_class,
    ):

        # Setup mock client
        mock_client = MagicMock()
        mock_client.get_tools = AsyncMock(return_value=[])
        mock_client_class.return_value = mock_client

        # Initial run
        middleware = ToolkitInjectorMiddleware(scan_root=project_root)
        assert mock_run.call_count == 1

        # Update version in pyproject.toml
        tk_path = project_root / ".ciri" / "toolkits" / "test_toolkit"
        (tk_path / "pyproject.toml").write_text("""
[project]
name = "test_toolkit"
version = "0.2.0"
dependencies = ["fastmcp"]
""")

        # Second run with same class level tracking
        # Reset mock
        mock_run.reset_mock()
        middleware2 = ToolkitInjectorMiddleware(scan_root=project_root)

        # Verify sync was called again due to version change
        assert mock_run.call_count == 1
        assert middleware2._toolkit_versions[str(tk_path.resolve())] == "0.2.0"
