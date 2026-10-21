def summarize_context(text: str, max_chars: int = 12000) -> str:
    """Apply a basic context cap; replace with relevance-aware summarization for production."""
    return text if len(text) <= max_chars else text[:max_chars] + "\n[Context truncated; retrieve missing evidence if needed.]"
