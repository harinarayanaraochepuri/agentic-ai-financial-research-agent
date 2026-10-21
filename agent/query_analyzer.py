def classify_query(query: str) -> str:
    q = query.lower()
    if any(w in q for w in ("compare", "versus", " vs ", "peers", "industry")):
        return "comparison"
    if any(w in q for w in ("risk", "threat", "exposure")):
        return "risk_assessment"
    if any(w in q for w in ("earnings", "revenue", "margin", "quarter")):
        return "financial_analysis"
    return "company_research"
