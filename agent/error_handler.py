import time
from typing import Callable, TypeVar
T = TypeVar("T")

def retry_call(fn: Callable[[], T], attempts: int = 3, base_delay: float = 1.0) -> T:
    """Retry an operation with bounded exponential backoff."""
    last_error = None
    for attempt in range(attempts):
        try:
            return fn()
        except Exception as exc:
            last_error = exc
            if attempt < attempts - 1:
                time.sleep(base_delay * (2 ** attempt))
    raise RuntimeError(f"Failed after {attempts} attempts: {last_error}") from last_error
