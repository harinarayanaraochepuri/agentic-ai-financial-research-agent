# ARA-1 Architecture Specification — starter

## Objective
Create an autonomous research assistant that retrieves evidence, synthesizes findings, checks claims, and produces a structured report.

## Agent pattern
Use a ReAct-style loop through LangGraph. The LLM selects tools from a registry, observes tool results, and continues until it can answer or reaches runtime/provider limits.

## Components
- Orchestration: LangGraph and ChatOpenAI.
- Registry: SEC EDGAR, market data, web search, transcript search, sentiment, memory, peer comparison, calculations, report generation, fact checking.
- Short-term memory: messages and observations within the current graph run.
- Long-term semantic memory: Chroma vector database with embeddings.
- Episodic memory: JSONL history of queries and report previews.
- Synthesis: preserve provenance; check periods, units, and definitions; disclose unresolved conflicts.
- Guardrails: no fabricated data, bounded retries, transparent gaps, no personalized investment advice.

## Known limitations
Transcript retrieval is search-based, sentiment is a lexical heuristic, fact checking is preliminary, and the PDF's targets must be tested rather than assumed.
