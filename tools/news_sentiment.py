from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
POS = {"growth", "beat", "strong", "record", "surge", "profit", "upgrade", "positive", "gain"}
NEG = {"loss", "miss", "decline", "drop", "weak", "lawsuit", "probe", "risk", "cut", "negative", "fall"}

@tool
def news_sentiment(query: str) -> str:
    """Search news and estimate text polarity with a basic word-count heuristic; not a validated finance model."""
    try:
        text = DuckDuckGoSearchRun().run(query)
        words = [w.strip(".,:;!?()[]{}").lower() for w in text.split()]
        pos, neg = sum(w in POS for w in words), sum(w in NEG for w in words)
        label = "positive-leaning" if pos > neg else "negative-leaning" if neg > pos else "mixed/neutral"
        return f"Lexical heuristic: {label} (positive terms={pos}, negative terms={neg}); noisy and not investor sentiment.\n{text}"
    except Exception as exc:
        return f"News search failed: {type(exc).__name__}: {exc}"
