def describe_conflict(metric: str, value_a: str, source_a: str, value_b: str, source_b: str) -> str:
    """Document conflicting values rather than silently choosing one."""
    return (f"Conflict for {metric}: {source_a} reports {value_a}; {source_b} reports {value_b}. "
            "Check reporting period, currency, units, definitions, and restatements. If unresolved, show both.")
