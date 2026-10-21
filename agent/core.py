import os
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from agent.prompts import SYSTEM_PROMPT
from tools.tool_registry import get_tools

def build_agent():
    """Create the LangGraph ReAct agent and tool registry."""
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY missing. Configure it in .env.")
    model = ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"), temperature=0)
    return create_react_agent(model, get_tools(), prompt=SYSTEM_PROMPT)
