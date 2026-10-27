import yfinance as yf

def fetch_stock_data(symbol):

    stock = yf.Ticker(symbol)

    data = stock.history(period="1y")

    data.rename(columns={
        "Open": "open_price",
        "High": "high_price",
        "Low": "low_price",
        "Close": "close_price",
        "Volume": "volume"
    }, inplace=True)

    return data