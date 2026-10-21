import os
import requests
from langchain_core.tools import tool

def _json(url):
    headers = {"User-Agent": os.getenv("SEC_USER_AGENT", "ARA-1 research contact@example.com")}
    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()
    return response.json()

def _cik(ticker):
    tickers = _json("https://www.sec.gov/files/company_tickers.json")
    row = next((x for x in tickers.values() if x.get("ticker", "").upper() == ticker.upper()), None)
    return str(row["cik_str"]).zfill(10) if row else None

@tool
def sec_filing_search(ticker: str, filing_type: str = "10-K") -> str:
    """Retrieve recent official SEC EDGAR filings for a US-listed company ticker and filing type."""
    try:
        cik = _cik(ticker)
        if not cik: return f"No SEC ticker match for {ticker}; verify the ticker."
        recent = _json(f"https://data.sec.gov/submissions/CIK{cik}.json").get("filings", {}).get("recent", {})
        rows = []
        for form, date, accession, doc in zip(recent.get("form", []), recent.get("filingDate", []), recent.get("accessionNumber", []), recent.get("primaryDocument", [])):
            if form == filing_type:
                url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession.replace('-', '')}/{doc}"
                rows.append(f"- {date} | {form} | {url}")
            if len(rows) >= 5: break
        return f"Recent SEC filings for {ticker.upper()}:\n" + ("\n".join(rows) or f"No recent {filing_type} found.")
    except Exception as exc:
        return f"SEC filing lookup failed: {type(exc).__name__}: {exc}"

@tool
def sec_company_facts(ticker: str) -> str:
    """Retrieve selected reported financial facts from the SEC company-facts endpoint."""
    try:
        cik = _cik(ticker)
        if not cik: return f"No SEC ticker match for {ticker}."
        facts = _json(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json")
        gaap = facts.get("facts", {}).get("us-gaap", {})
        out = []
        for concept in ("RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "NetIncomeLoss", "Assets"):
            item = gaap.get(concept, {})
            for unit, entries in item.get("units", {}).items():
                for e in entries[-4:]:
                    out.append(f"{concept}: end={e.get('end')}, value={e.get('val')} {unit}, form={e.get('form')}, filed={e.get('filed')}")
        return f"SEC company facts for {facts.get('entityName', ticker)}:\n" + ("\n".join(out[-20:]) or "No selected facts found. Check concept names and reporting periods.")
    except Exception as exc:
        return f"SEC company facts failed: {type(exc).__name__}: {exc}"
