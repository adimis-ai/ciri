import os
import asyncio
import sys
import uuid
from typing import Optional, List, Any, Dict, Union

# Third-party imports
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

# LangGraph / LangChain imports
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore
from langchain_core.messages import HumanMessage, AIMessage, BaseMessageChunk
from langgraph.types import Command

# Local imports
from .agent import Ciri, LLMConfig, ResumeCommand
from .utils import get_default_filesystem_root
from .serializers import CiriJsonPlusSerializer

console = Console()

async def interactive_chat():
    """Main interactive chat loop for CIRI CLI."""
    console.print(Panel("[bold cyan]CIRI[/bold cyan] - Desktop Personal AI Copilot\n[dim]Initializing...[/dim]", border_style="cyan"))

    # Initialize Ciri with default config
    # Ensure required environment variables are set
    if not os.getenv("OPENROUTER_API_KEY"):
        console.print("[yellow]OPENROUTER_API_KEY not found in environment.[/yellow]")
        api_key = Prompt.ask("Please enter your [bold]OpenRouter API Key[/bold]", password=True)
        if api_key:
            os.environ["OPENROUTER_API_KEY"] = api_key
            console.print("[green]API Key set for this session.[/green]")
        else:
            console.print("[red]API Key is required to continue. Exiting.[/red]")
            return

    model = os.getenv("CIRI_MODEL")
    if not model:
        console.print("[yellow]CIRI_MODEL not found in environment.[/yellow]")
        model = Prompt.ask("Please enter the [bold]Model name[/bold]", default="openai/gpt-5-mini")
        os.environ["CIRI_MODEL"] = model
        console.print(f"[green]Model set to {model} for this session.[/green]")

    llm_config = LLMConfig(model=model)
    
    ciri_app = Ciri(llm_config=llm_config)
    
    # Checkpointer and Store
    # Use CiriJsonPlusSerializer to handle Send objects and other complex types
    checkpointer = InMemorySaver(serde=CiriJsonPlusSerializer())
    store = InMemoryStore()
    
    # Compile the agent graph
    graph = ciri_app.compile(store=store, checkpointer=checkpointer)
    
    thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}
    
    console.print(f"[green]Ready![/green] Root directory: [bold]{os.getcwd()}[/bold]\n")

    while True:
        try:
            user_input = Prompt.ask("[bold green]You[/bold green]")
            if user_input.lower() in ("exit", "quit", "bye"):
                console.print("[cyan]Goodbye![/cyan]")
                break
            
            if not user_input.strip():
                continue

            # Initial input or resume
            inputs = {"messages": [HumanMessage(content=user_input)]}
            
            await run_graph(graph, inputs, config)
            
        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted by user. Type 'exit' to quit.[/yellow]")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")

async def run_graph(graph, inputs, config):
    """Run the graph and handle streaming output and interrupts."""
    current_ai_message = ""
    prefix_printed = False
    seen_tool_call_ids = set()
    
    from langchain_core.messages import ToolMessage

    # Use console.status to show "Thinking..." while waiting for the first token
    with console.status("[bold blue]Thinking...", spinner="dots") as status:
        # Use astream for real-time messaging
        # stream_mode="messages" streams chunks of messages
        async for chunk in graph.astream(inputs, config, stream_mode="messages"):
            message, metadata = chunk
            
            # Update status or print based on message type
            if isinstance(message, BaseMessageChunk):
                # If we have content, stop the spinner and start printing
                if message.content:
                    status.stop()
                    
                    if not prefix_printed:
                        console.print("[bold cyan]CIRI:[/bold cyan] ", end="")
                        prefix_printed = True
                    
                    content = message.content
                    if isinstance(content, str):
                        console.print(content, end="")
                        current_ai_message += content
                    elif isinstance(content, list):
                        for part in content:
                            if isinstance(part, dict) and part.get("type") == "text":
                                text = part.get("text", "")
                                console.print(text, end="")
                                current_ai_message += text
                
                # Inform about tool calls if any
                if hasattr(message, "tool_calls") and message.tool_calls:
                    for tool_call in message.tool_calls:
                        tc_id = tool_call.get("id")
                        if tc_id and tc_id not in seen_tool_call_ids and tool_call.get("name"):
                            status.stop()
                            console.print(f"\n[bold yellow]🛠️  Action:[/bold yellow] [cyan]{tool_call['name']}[/cyan]([dim]{tool_call['args']}[/dim])")
                            seen_tool_call_ids.add(tc_id)
            
            elif isinstance(message, ToolMessage):
                status.stop()
                # Print tool result summary
                content_preview = str(message.content)[:200] + "..." if len(str(message.content)) > 200 else str(message.content)
                console.print(f"\n[bold magenta]🔧 Component Output:[/bold magenta] [dim]{content_preview}[/dim]")
                # Resume thinking while waiting for the next AI move
                status.start()

    console.print("\n") # New line after the response

    # Check for interrupts
    state = await graph.aget_state(config)
    if state.next:
        # We have an interrupt
        snapshot = state.values
        interrupts = snapshot.get("__interrupt__", [])
        
        if interrupts:
            for interrupt_val in interrupts:
                val = interrupt_val.get("value")
                if not val:
                    continue
                
                # Handle human_follow_up
                if isinstance(val, dict) and val.get("type") == "human_follow_up":
                    question = val.get("question")
                    options = val.get("options")
                    
                    console.print(Panel(f"[bold yellow]Follow-up Question:[/bold yellow]\n{question}", border_style="yellow"))
                    
                    if options:
                        console.print(f"Options: {', '.join(options)}")
                        response = Prompt.ask("Choose an option", choices=options)
                    else:
                        response = Prompt.ask("Your response")
                    
                    # Resume with user response
                    await run_graph(graph, Command(resume=response), config)
                
                # Handle tool approval (if any custom ones configured via deepagents)
                elif isinstance(val, dict) and "action_requests" in val:
                    # This is likely the tool approval interrupt from HumanInLoopMiddleware
                    console.print(Panel("[bold yellow]Tool Execution Approval Required[/bold yellow]", border_style="yellow"))
                    for req in val["action_requests"]:
                        console.print(f"Tool: [bold]{req['name']}[/bold]")
                        console.print(f"Arguments: {req.get('arguments')}")
                    
                    decision = Prompt.ask("Action", choices=["approve", "reject", "edit"], default="approve")
                    
                    if decision == "approve":
                        command = Command(resume={"decisions": [{"type": "approve"}]})
                    elif decision == "reject":
                        reason = Prompt.ask("Reason for rejection", default="Not allowed")
                        command = Command(resume={"decisions": [{"type": "reject", "message": reason}]})
                    else: # edit
                        # Simple edit for now - just ask for new args as JSON or similar
                        # In a real CLI we might want a proper editor
                        console.print("Editing not fully implemented in CLI, rejecting instead.")
                        command = Command(resume={"decisions": [{"type": "reject", "message": "Editing not supported via CLI"}]})
                    
                    await run_graph(graph, command, config)

def main():
    """EntryPoint for the CIRI CLI."""
    asyncio.run(interactive_chat())

if __name__ == "__main__":
    main()
