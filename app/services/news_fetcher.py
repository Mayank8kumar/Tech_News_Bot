import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_latest_tech_news(country="in", page_size=10):
    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"category=technology&"
        f"country={country}&"
        f"pageSize={page_size}&"
        f"apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"News API error: {response.status_code}")

    data = response.json()
    return data["articles"]
