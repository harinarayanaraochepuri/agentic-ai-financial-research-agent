def source_reliability(source_type: str) -> int:
    """Simple source priority: smaller rank means higher priority."""
    return {"sec_filing": 1, "official_company_filing": 1, "financial_api": 2,
            "earnings_transcript": 3, "news": 4, "social_media": 5}.get(source_type.lower(), 99)
