from langchain_core.tools import tool

@tool
def fact_checker(claim: str, source_text: str) -> str:
    """Check textual overlap between a claim and source text; preliminary only, not proof of truth."""
    tokens = [t.strip(".,:;!?()[]{}").lower() for t in claim.split() if len(t.strip(".,:;!?()[]{}")) > 3]
    source = " ".join(source_text.lower().split())
    hits = [t for t in tokens if t in source]
    ratio = len(hits) / max(1, len(set(tokens)))
    status = "partial textual support" if ratio >= 0.5 else "weak/no textual support"
    return f"Lexical overlap={ratio:.0%}; {status}. Verify the original source; overlap does not establish truth."
