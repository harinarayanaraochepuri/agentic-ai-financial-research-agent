from tools.sec_edgar import sec_filing_search, sec_company_facts
from tools.financial_api import financial_data_api, company_profile, peer_comparison, calculation_engine
from tools.web_search import web_search, earnings_transcript_search
from tools.news_sentiment import news_sentiment
from memory.vector_store import vector_db_search, vector_db_store
from tools.fact_checker import fact_checker
from tools.report_gen import report_generator

def get_tools():
    """Return all registered tools (13 total)."""
    return [sec_filing_search, sec_company_facts, financial_data_api, web_search,
            earnings_transcript_search, news_sentiment, vector_db_search, vector_db_store,
            company_profile, peer_comparison, report_generator, fact_checker, calculation_engine]
