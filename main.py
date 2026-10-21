from __future__ import annotations
import argparse
from pathlib import Path
from dotenv import load_dotenv
from agent.core import build_agent
from memory.episodic import save_episode

def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description="ARA-1 financial research agent")
    parser.add_argument("query")
    parser.add_argument("--output", default="results/generated/research_report.md")
    args = parser.parse_args()
    result = build_agent().invoke({"messages": [{"role": "user", "content": args.query}]})
    messages = result.get("messages", [])
    report = str(messages[-1].content) if messages else "No response returned."
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")
    save_episode(args.query, report)
    print(f"Report saved to {out.resolve()}")
    print(report)

if __name__ == "__main__":
    main()
