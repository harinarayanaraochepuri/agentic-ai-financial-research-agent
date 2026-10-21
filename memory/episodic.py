import json, os
from datetime import datetime, timezone
from pathlib import Path

def save_episode(query: str, outcome: str) -> None:
    """Append a short episode record after a research run."""
    path = Path(os.getenv("EPISODIC_MEMORY_PATH", "./data/episodic_memory.jsonl"))
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {"timestamp": datetime.now(timezone.utc).isoformat(), "query": query, "outcome_preview": outcome[:1200]}
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
