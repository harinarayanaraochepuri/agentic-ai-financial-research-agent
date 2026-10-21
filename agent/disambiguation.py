def disambiguate(query: str) -> dict:
    """Flag a few common ambiguous queries; do not silently guess."""
    if query.strip().lower() in {"analyze amazon", "research amazon", "what's happening with the banks?"}:
        return {"ambiguous": True, "message": "Clarify the company/business unit, geography, or period."}
    return {"ambiguous": False, "message": "No obvious ambiguity detected; disclose assumptions if needed."}
