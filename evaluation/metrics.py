METRIC_CHECKLIST = {
"factual_accuracy": ["numerical_accuracy_rate", "citation_accuracy", "temporal_accuracy", "entity_accuracy", "hallucination_rate"],
"completeness": ["section_coverage", "data_source_diversity", "temporal_coverage", "risk_factor_coverage"],
"analytical_depth": ["insight_density", "cross_source_synthesis", "quantitative_reasoning", "forward_looking_analysis"],
"coherence": ["logical_flow", "internal_consistency", "executive_summary_quality", "professional_formatting"],
"agent_behaviour": ["tool_efficiency", "error_recovery_rate", "planning_quality", "memory_utilization", "latency"],
}
def empty_scorecard():
    """Return a blank scorecard; populate only with measured results."""
    return {category: {metric: None for metric in metrics} for category, metrics in METRIC_CHECKLIST.items()}
