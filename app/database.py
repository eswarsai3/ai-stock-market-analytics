import mysql.connector
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return connection

#mysql connector

import pandas as pd

def save_stock_data(symbol, data):
    connection = connect_db()
    cursor = connection.cursor()

    sql = """
    INSERT IGNORE INTO stock_prices
    (
        symbol,
        trade_date,
        open_price,
        high_price,
        low_price,
        close_price,
        volume,

        SMA_10,
        SMA_20,
        SMA_50,
        SMA_100,
        SMA_200,

        EMA_10,
        EMA_20,
        EMA_50,
        EMA_100,
        EMA_200,

        RSI,
        MACD,
        Signal_Line,

        Middle_Band,
        Upper_Band,
        Lower_Band
    )
    VALUES
    (
        %s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,
        %s,%s,%s,
        %s,%s,%s
    )
    """

    for index, row in data.iterrows():

        values = (
            symbol,
            index.date(),

            float(row["open_price"]),
            float(row["high_price"]),
            float(row["low_price"]),
            float(row["close_price"]),
            int(row["volume"]),
            float(row["SMA_10"]) if pd.notna(row["SMA_10"]) else None,
            float(row["SMA_20"]) if pd.notna(row["SMA_20"]) else None,
            float(row["SMA_50"]) if pd.notna(row["SMA_50"]) else None,
            float(row["SMA_100"]) if pd.notna(row["SMA_100"]) else None,
            float(row["SMA_200"]) if pd.notna(row["SMA_200"]) else None,

            float(row["EMA_10"]) if pd.notna(row["EMA_10"]) else None,
            float(row["EMA_20"]) if pd.notna(row["EMA_20"]) else None,
            float(row["EMA_50"]) if pd.notna(row["EMA_50"]) else None,
            float(row["EMA_100"]) if pd.notna(row["EMA_100"]) else None,
            float(row["EMA_200"]) if pd.notna(row["EMA_200"]) else None,

            float(row["RSI"]) if pd.notna(row["RSI"]) else None,
            float(row["MACD"]) if pd.notna(row["MACD"]) else None,
            float(row["Signal_Line"]) if pd.notna(row["Signal_Line"]) else None,

            float(row["Middle_Band"]) if pd.notna(row["Middle_Band"]) else None,
            float(row["Upper_Band"]) if pd.notna(row["Upper_Band"]) else None,
            float(row["Lower_Band"]) if pd.notna(row["Lower_Band"]) else None
        )

        cursor.execute(sql, values)

    connection.commit()

    cursor.close()
    connection.close()

import pandas as pd

def get_stock_data(symbol):
    connection = connect_db()

    query = """
    SELECT
        trade_date,
        open_price,
        high_price,
        low_price,
        close_price,
        volume
    FROM stock_prices
    WHERE symbol = %s
    ORDER BY trade_date;
    """

    df = pd.read_sql(query, connection, params=(symbol,))

    connection.close()

    return df