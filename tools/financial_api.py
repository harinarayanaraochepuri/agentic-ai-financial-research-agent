import yfinance as yf
from langchain_core.tools import tool

@tool
def financial_data_api(ticker: str) -> str:
    """Retrieve recent financial statements and metadata via yfinance; verify key values against filings."""
    try:
        obj = yf.Ticker(ticker)
        info = obj.get_info()
        def summary(frame, label):
            return f"{label}:\n{frame.iloc[:8, :4].to_string()}" if frame is not None and not frame.empty else f"{label}: unavailable"
        meta = {k: info.get(k) for k in ("longName", "currency", "sector", "industry", "marketCap", "currentPrice")}
        return f"Provider metadata (may be delayed/incomplete): {meta}\n\n{summary(obj.income_stmt, 'Income statement')}\n\n{summary(obj.balance_sheet, 'Balance sheet')}\n\n{summary(obj.cashflow, 'Cash flow')}"
    except Exception as exc:
        return f"Financial data provider failed: {type(exc).__name__}: {exc}"

@tool
def company_profile(ticker: str) -> str:
    """Retrieve basic company profile and business description from yfinance."""
    try:
        info = yf.Ticker(ticker).get_info()
        keys = ("longName", "symbol", "longBusinessSummary", "sector", "industry", "country", "website", "marketCap", "currency", "fullTimeEmployees")
        return "\n".join(f"{k}: {info.get(k)}" for k in keys)
    except Exception as exc:
        return f"Profile lookup failed: {type(exc).__name__}: {exc}"

@tool
def peer_comparison(ticker: str, peers: str = "") -> str:
    """Compare selected public-company metrics for a ticker and comma-separated peer tickers."""
    try:
        symbols = [ticker.upper()] + [x.strip().upper() for x in peers.split(",") if x.strip()]
        defaults = {"MSFT": ["GOOGL", "AMZN"], "NVDA": ["AMD", "AVGO"], "AAPL": ["MSFT", "GOOGL"]}
        if len(symbols) == 1: symbols += defaults.get(symbols[0], [])
        rows = []
        for symbol in symbols[:6]:
            info = yf.Ticker(symbol).get_info()
            rows.append({k: info.get(k) for k in ("shortName", "symbol", "sector", "marketCap", "trailingPE", "profitMargins", "revenueGrowth", "currency")})
        return "Provider peer metrics (periods/definitions may differ):\n" + "\n".join(map(str, rows))
    except Exception as exc:
        return f"Peer comparison failed: {type(exc).__name__}: {exc}"

@tool
def calculation_engine(calculation_type: str, a: float, b: float) -> str:
    """Calculate growth_rate (a=current,b=prior), percent_change (a=new,b=old), or margin (a=profit,b=revenue)."""
    kind = calculation_type.lower()
    if b == 0: return "Cannot calculate when denominator/prior value is zero."
    if kind in {"growth_rate", "percent_change"}: return f"{kind}: {((a-b)/abs(b))*100:.2f}%"
    if kind == "margin": return f"margin: {(a/b)*100:.2f}%"
    return "Unsupported type; use growth_rate, percent_change, or margin."
