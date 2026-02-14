"""TODO:
Create an AgentMiddleware that allows the defination of toolkits in `.ciri/toolkits` directory and even in the nested directories of the root directory other that .ciri directory. Each toolkit in toolkits folder of .ciri folder should have its own directory with a pyproject.toml file and a main.py file that exposes a local MCP server using UV and FastMCP. The structure of the toolkit directory should be as follows:


```
<root_dir>/.ciri/
└── toolkits/
    └── <toolkit_name>/
        ├── README.md
        ├── pyproject.toml
        └── src/
            └── main.py  # Exposes a local MCP server using UV and FastMCP
```

Ensure pyproject toml contains a fastmcp dependency and a main.py that exposes a local MCP server using UV and FastMCP so that when we call `uv run src/main.py` it starts the MCP server for this toolkit.

If a toolkit server is already running:
    - Restart only when `.ciri/toolkit/<toolkit_name>/pyproject.toml` version changes.
    - Before starting/restarting, install & sync latest dependencies using **uv**.

For all the toolkit mcp server that are running we need to get their tools using MultiServerMCPClient supporting all the connection types (StdioConnection, SSEConnection, StreamableHttpConnection, WebsocketConnection) and set them in self.tools of the ToolkitInjectorMiddleware. This way we can inject the tools from the toolkits into the agent's context and use them in the agent's execution.

Ensure we are not including tool in self.tools that already exists in self.already_available_tools to avoid duplication of tools in the agent's context.
"""

from langchain.agents.middleware import AgentMiddleware
from langchain_mcp_adapters.client import (
    MultiServerMCPClient,
    StdioConnection,
    SSEConnection,
    StreamableHttpConnection,
    WebsocketConnection,
)


class ToolkitInjectorMiddleware(AgentMiddleware):
    def __init__(self):
        super().__init__()
        self.tools = []
