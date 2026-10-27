def calculate_sma(df):

    periods = [10, 20, 50, 100, 200]
    for period in periods:
        df[f"SMA_{period}"] = (
            df["close_price"]
            .rolling(window=period)
            .mean()
        )
    return df

def calculate_ema(df):

    periods = [10, 20, 50, 100, 200]

    for period in periods:
        df[f"EMA_{period}"] = (
            df["close_price"]
            .ewm(span=period, adjust=False)
            .mean()
        )

    return df

def calculate_rsi(df, period=14):

    delta = df["close_price"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))

    return df

def calculate_macd(df):

    ema12 = df["close_price"].ewm(span=12, adjust=False).mean()

    ema26 = df["close_price"].ewm(span=26, adjust=False).mean()

    df["MACD"] = ema12 - ema26

    df["Signal_Line"] = (
        df["MACD"]
        .ewm(span=9, adjust=False)
        .mean()
    )

    return df

def calculate_bollinger(df):

    df["Middle_Band"] = (
        df["close_price"]
        .rolling(window=20)
        .mean()
    )

    std = (
        df["close_price"]
        .rolling(window=20)
        .std()
    )

    df["Upper_Band"] = df["Middle_Band"] + (2 * std)

    df["Lower_Band"] = df["Middle_Band"] - (2 * std)

    return df

def detect_trend(df):

    latest = df.iloc[-1]
    if latest["SMA_50"] > latest["SMA_200"]:
        return "Bullish"

    elif latest["SMA_50"] < latest["SMA_200"]:
        return "Bearish"

    else:
        return "Sideways"

def generate_signal(df):

    latest = df.iloc[-1]

    if latest["RSI"] < 30:
        return "BUY"

    elif latest["RSI"] > 70:
        return "SELL"

    else:
        return "HOLD"


def analyze_stock(df):

    df = calculate_sma(df)
    df = calculate_ema(df)
    df = calculate_rsi(df)
    df = calculate_macd(df)
    df = calculate_bollinger(df)
    trend = detect_trend(df)
    signal = generate_signal(df)
    return df, trend, signal