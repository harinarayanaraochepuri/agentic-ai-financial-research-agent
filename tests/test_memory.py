from memory.context_manager import summarize_context

def test_context_cap_adds_notice():
    assert "truncated" in summarize_context("x" * 50, max_chars=10)
