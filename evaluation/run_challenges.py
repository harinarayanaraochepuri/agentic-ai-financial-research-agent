import argparse
from pathlib import Path
from evaluation.challenges import CHALLENGES
from agent.core import build_agent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--challenge", default="challenge_1", choices=[x[0] for x in CHALLENGES])
    args = parser.parse_args()
    query = dict(CHALLENGES)[args.challenge]
    result = build_agent().invoke({"messages": [{"role": "user", "content": query}]})
    messages = result.get("messages", [])
    report = str(messages[-1].content) if messages else "No response."
    out = Path("results") / f"{args.challenge}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")
    print(f"Saved {out}")

if __name__ == "__main__":
    main()
