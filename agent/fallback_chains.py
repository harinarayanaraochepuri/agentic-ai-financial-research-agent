def try_fallbacks(operations):
    """Try provider functions in order and record failures."""
    errors = []
    for index, operation in enumerate(operations):
        try:
            return {"ok": True, "fallback_index": index, "data": operation(), "errors": errors}
        except Exception as exc:
            errors.append(f"{type(exc).__name__}: {exc}")
    return {"ok": False, "data": None, "errors": errors}
