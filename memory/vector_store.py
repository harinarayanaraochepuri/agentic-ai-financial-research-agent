import os
from pathlib import Path
from langchain_core.tools import tool
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

def get_store():
    path = Path(os.getenv("CHROMA_DIR", "./data/chroma"))
    path.mkdir(parents=True, exist_ok=True)
    return Chroma(collection_name="ara1_research_memory", embedding_function=OpenAIEmbeddings(model="text-embedding-3-small"), persist_directory=str(path))

@tool
def vector_db_search(query: str) -> str:
    """Search long-term semantic memory for relevant previously stored research."""
    try:
        docs = get_store().similarity_search(query, k=4)
        return "\n\n".join(f"metadata={d.metadata}\n{d.page_content}" for d in docs) if docs else "No relevant memory found."
    except Exception as exc:
        return f"Vector search unavailable: {type(exc).__name__}: {exc}"

@tool
def vector_db_store(content: str, ticker: str = "UNKNOWN", source_type: str = "research", confidence: float = 0.5) -> str:
    """Store research findings in persistent vector memory with metadata."""
    try:
        get_store().add_texts([content], metadatas=[{"ticker": ticker.upper(), "source_type": source_type, "confidence": float(confidence)}])
        return f"Stored research memory for {ticker.upper()}."
    except Exception as exc:
        return f"Vector store failed: {type(exc).__name__}: {exc}"
