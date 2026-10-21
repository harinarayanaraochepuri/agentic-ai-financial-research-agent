from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

@tool
def web_search(query: str) -> str:
    """Search the web for current news, industry context, and source references."""
    try: return DuckDuckGoSearchRun().run(query)
    except Exception as exc: return f"Web search failed: {type(exc).__name__}: {exc}"

@tool
def earnings_transcript_search(ticker: str, quarter_year: str = "most recent") -> str:
    """Search for a public earnings-call transcript or prepared remarks; availability varies by company."""
    query = f"{ticker} {quarter_year} earnings call transcript investor relations"
    try: return f"Query: {query}\n" + DuckDuckGoSearchRun().run(query)
    except Exception as exc: return f"Transcript search failed: {type(exc).__name__}: {exc}"
