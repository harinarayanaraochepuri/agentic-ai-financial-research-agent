from langchain_core.tools import tool

@tool
def report_generator(company: str, findings: str) -> str:
    """Format collected evidence into a structured Markdown research report without inventing missing facts."""
    return f"""# Financial Research Report: {company}

## 1. Executive Summary
Summarize only supported conclusions and disclose information gaps.

## 2. Company Overview
Describe the company, sector, business segments, and relevant context with sources.

## 3. Financial Analysis
State values with reporting periods, units, currency, and citations.

## 4. Risk Assessment
Separate disclosed risks, recent developments, and analytical inferences.

## 5. Competitive Position
Compare only reasonably comparable metrics and explain limitations.

## 6. Outlook and Scenarios
State assumptions; scenarios are not predictions.

## 7. Research Methodology and Limitations
Describe sources, gaps, conflicts, and verification limits.

## 8. Sources and Findings
{findings}

Educational research only; not investment advice.
"""
