import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
load_dotenv()

API_KEY = os.getenv("MARKETAUX_API_KEY")


def get_stock_news(company):

    url = "https://api.marketaux.com/v1/news/all"
    today = datetime.today()
    from_date = today - timedelta(days=30)
    params = {
        "api_token": API_KEY,
        "search": company,
        "language": "en",
        "published_after": from_date.strftime("%Y-%m-%dT00:00"),
        "published_before": today.strftime("%Y-%m-%dT23:59"),
        "limit": 5
    }

    response = requests.get(url, params=params)

    print("Status:", response.status_code)

    if response.status_code != 200:
        print(response.text)
        return []

    return response.json()


if __name__ == "__main__":

    news = get_stock_news("Tata Consultancy Services")

    print(news)