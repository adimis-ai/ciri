from typing import Optional
from deepagents import CompiledSubAgent
from langchain.agents import create_agent
from langchain.chat_models import BaseChatModel
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser
from langchain.agents.middleware import (
    TodoListMiddleware,
    ToolRetryMiddleware,
    SummarizationMiddleware,
)

from ..toolkit.web_crawler_tool import (
    build_web_crawler_tool,
    BrowserConfig as CrawlerBrowserConfig,
)

WEB_RESEARCHER_SYSTEM_PROMPT = """"""


def get_playwright_tools():
    browser = create_async_playwright_browser()
    toolkit = PlayWrightBrowserToolkit.from_browser(browser)
    return toolkit.get_tools()


def build_web_researcher_agent(
    model: BaseChatModel, crawler_browser_config: Optional[CrawlerBrowserConfig] = None
) -> CompiledSubAgent:
    tools = get_playwright_tools()
    tools.extend([DuckDuckGoSearchResults(name="simple_web_search")])
    tools.append(build_web_crawler_tool(crawler_browser_config))

    agent = create_agent(
        tools,
        model,
        name="Web Researcher Agent",
        system_prompt=WEB_RESEARCHER_SYSTEM_PROMPT,
        middleware=[TodoListMiddleware(), SummarizationMiddleware(model=model)],
    )

    return CompiledSubAgent(
        runnable=agent,
        name="Web Researcher",
        description="A sub-agent that can perform web research using Playwright.",
    )
