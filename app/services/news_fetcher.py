import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GNEWS_API_KEY= os.getenv("GNEWS_API_KEY")


def fetch_tech_news(country="in", page_size=10):
    """
    Fetch latest tech news headlines from NewsAPI.
    Returns simplified list of articles with essential metadata.
    """
    # url = (
    #     f"https://newsapi.org/v2/top-headlines?"
    #     f"category=technology&"
    #     f"country={country}&"
    #     f"pageSize={page_size}&"
    #     f"apiKey={NEWS_API_KEY}"
    # )

    url = (
    "https://newsapi.org/v2/everything?"
    "q=technology&"
    "language=en&"
    "sortBy=publishedAt&"
    f"pageSize={page_size}&"
    f"apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"News API error: {response.status_code} - {response.text}")

    data = response.json()
    # print("We got the data............")
    if data.get("status") != "ok":
        raise Exception("Failed to fetch news")

    # Simplify and return useful parts
    simplified_articles = []
    # print("Extracting the relevant data.........")
    for article in data.get("articles", []):
        simplified_articles.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url"),
            "source": article.get("source", {}).get("name"),
            "publishedAt": article.get("publishedAt")
        })

    return simplified_articles



def fetch_tech_news_Gnews(country="in", page_size=10):
    """
    Fetch latest tech news headlines from NewsAPI.
    Returns simplified list of articles with essential metadata.
    """
    url = (
        f"https://gnews.io/api/v4/top-headlines?"
        f"category=technology&"
        f"country={country}&"
        f"pageSize={page_size}&"
        f"apiKey={GNEWS_API_KEY}"
    )

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"News API error: {response.status_code} - {response.text}")

    data = response.json()
    # print("We got the data............")
    if data.get("status") != "ok":
        raise Exception("Failed to fetch news")

    # Simplify and return useful parts
    simplified_articles = []
    # print("Extracting the relevant data.........")
    for article in data.get("articles", []):
        simplified_articles.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "content":article.get("content"),
            "url": article.get("url"),
            "source": article.get("source", {}).get("name"),
            "publishedAt": article.get("publishedAt")
        })

    return simplified_articles
