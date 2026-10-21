from synthesis.engine import source_reliability
from synthesis.conflict_resolver import describe_conflict

def test_sec_ranked_above_news():
    assert source_reliability("sec_filing") < source_reliability("news")

def test_conflicts_are_documented():
    note = describe_conflict("revenue", "$10B", "source A", "$9B", "source B")
    assert "$10B" in note and "$9B" in note and "Check reporting period" in note
