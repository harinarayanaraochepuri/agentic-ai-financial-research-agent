# ARA-1 — Autonomous Financial Research Agent

A beginner-friendly Python starter for an autonomous, source-backed financial research agent using LangGraph, financial-data tools, SEC EDGAR, web search, and Chroma memory.

**Educational use only.** This is not a financial adviser and does not make buy/sell recommendations. Providers may return incomplete, delayed, or incorrect data. Verify material claims against original filings.

## Install

Use Python 3.10 or 3.11:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, set `OPENAI_API_KEY`, and replace the SEC user agent with a real contact email. Never commit `.env`.

## Run

```bash
python main.py "Analyze NVIDIA's recent financial performance, competitive position, and key risks"
```

Optional output path:

```bash
python main.py "Create a profile of Microsoft" --output results/microsoft_profile.md
```

Run tests with `python -m pytest`.

## Implemented tools (13)

1. SEC filing search
2. SEC company facts
3. Financial data lookup
4. Web search
5. Earnings transcript search
6. News sentiment heuristic
7. Vector-memory search
8. Vector-memory storage
9. Company profile
10. Peer comparison
11. Report generator
12. Fact checker
13. Calculation engine

## Memory layers

- Short-term: current LangGraph message/tool state.
- Long-term semantic: persistent Chroma vector store.
- Episodic: JSONL records of queries and report previews.

## Important limitations

The transcript tool is search-based, sentiment is a basic word-count heuristic, and fact checking is preliminary lexical overlap—not a complete claim-verification system. The scaffold has not passed the PDF's evaluation targets until you run the challenges and measure results. Complete the architecture specification, eight challenge reports, evaluation evidence, trace gallery, optimization log, and error log before formal submission.

## AI assistance disclosure

This scaffold was created with AI assistance. Review, run, customize, and understand the code before submitting it. Document AI tools used and explain your own architectural decisions.
