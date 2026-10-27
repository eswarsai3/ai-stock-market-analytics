import plotly.graph_objects as go

def show_dashboard(df, symbol):

    df = df.reset_index()

    print(df.columns)

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=df["Date"],
            open=df["open_price"],
            high=df["high_price"],
            low=df["low_price"],
            close=df["close_price"],
            name="Price"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["SMA_20"],
            mode="lines",
            name="SMA 20"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["SMA_50"],
            mode="lines",
            name="SMA 50"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["SMA_200"],
            mode="lines",
            name="SMA 200"
        )
    )

    fig.update_layout(
        title=f"{symbol} Stock Analysis",
        xaxis_title="Date",
        yaxis_title="Price",
        template="plotly_white",
        xaxis_rangeslider_visible=False,
        height=700
    )

    fig.show()