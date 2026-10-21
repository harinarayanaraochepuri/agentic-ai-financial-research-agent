def evidence_summary(findings: list[str]) -> str:
    """Join findings while keeping each source/tool result separated."""
    return "\n\n---\n\n".join(f"Finding {i+1}:\n{item}" for i, item in enumerate(findings))
