import os
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def prepare_prompt(df, trend, signal, news):

    latest = df.iloc[-1]
    news_text = ""

    for article in news.get("data", []):
        news_text += f"""
    Title: {article.get("title", "N/A")}
    Summary: {article.get("description", "No description")}
    Source: {article.get("source", "Unknown")}
    Published: {article.get("published_at", "Unknown")}
    ----------------------------------------
    """
    prompt = f"""
You are an expert stock market analyst.

Analyze the following stock based on the technical indicators.

Current Price: {latest["close_price"]:.2f}

SMA 20: {latest["SMA_20"]:.2f}
SMA 50: {latest["SMA_50"]:.2f}
SMA 100: {latest["SMA_100"]:.2f}
SMA 200: {latest["SMA_200"]:.2f}

EMA 20: {latest["EMA_20"]:.2f}
EMA 50: {latest["EMA_50"]:.2f}
EMA 100: {latest["EMA_100"]:.2f}
EMA 200: {latest["EMA_200"]:.2f}

RSI: {latest["RSI"]:.2f}

MACD: {latest["MACD"]:.2f}

Trend: {trend}

Recommendation: {signal}

Latest News: {news_text}
Explain:
1. Overall market trend.
2. RSI interpretation.
3. MACD interpretation.
4. Moving average analysis.
5. Analyze whether the latest news is positive, negative, or neutral.
6. Explain how the news may affect the stock price.
7. Risks to watch.
8. Explain whether the system recommendation is justified based on the technical indicators and latest news..

Keep the explanation simple and professional.
"""

    return prompt

def generate_ai_report(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

def analyze_with_ai(df, trend, signal,news):
    prompt = prepare_prompt(df, trend, signal,news)
    report = generate_ai_report(prompt)
    return report