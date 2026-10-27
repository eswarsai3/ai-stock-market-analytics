from data import fetch_stock_data
from database import save_stock_data, get_stock_data
from analysis import analyze_stock
from dashboard import show_dashboard
from ai import analyze_with_ai
from app.search import get_stock_symbol
from news import get_stock_news

def main():
    company = input("Enter Company Name: ")

    symbol = get_stock_symbol(company)

    if symbol is None:
        print("Company not found.")
        return

    print(f"Stock Symbol: {symbol}")
    print("\nDownloading latest stock data...")
    data = fetch_stock_data(symbol)

    if data.empty:
        print("Invalid Stock Symbol!")
        return
    print(data.columns)




    # df = get_stock_data(symbol)
    #
    # if df.empty:
    #     print("No data available.")
    #     return

    df, trend, signal = analyze_stock(data)
    save_stock_data(symbol, df)
    print("Database updated successfully.")
    news = get_stock_news(company)

    report = analyze_with_ai(df, trend, signal, news)
    print("\n========== AI REPORT ==========\n")
    print(report)
    show_dashboard(df, symbol)
    latest = df.iloc[-1]

    print("\n========== STOCK ANALYSIS ==========")

    print(f"Stock           : {symbol}")
    print(f"Current Price   : {latest['close_price']:.2f}")

    print("\nMoving Averages")

    print(f"SMA 20          : {latest['SMA_20']:.2f}")
    print(f"SMA 50          : {latest['SMA_50']:.2f}")
    print(f"SMA 200         : {latest['SMA_200']:.2f}")

    print(f"EMA 20          : {latest['EMA_20']:.2f}")

    print("\nIndicators")

    print(f"RSI             : {latest['RSI']:.2f}")
    print(f"MACD            : {latest['MACD']:.2f}")

    print("\nAnalysis")

    print(f"Trend           : {trend}")
    print(f"Recommendation  : {signal}")


if __name__ == "__main__":
    main()