import yfinance as yf


def get_stock_symbol(company):

    search = yf.Search(company, max_results=10)

    quotes = search.quotes

    if not quotes:
        return None

    # Prefer NSE stocks
    for quote in quotes:
        symbol = quote.get("symbol", "")

        if symbol.endswith(".NS"):
            return symbol

    # If NSE not found, prefer BSE
    for quote in quotes:
        symbol = quote.get("symbol", "")

        if symbol.endswith(".BO"):
            return symbol

    # Otherwise return the first result
    return quotes[0].get("symbol")