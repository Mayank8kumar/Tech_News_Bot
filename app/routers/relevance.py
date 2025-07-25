from fastapi import APIRouter
from app.services.news_fetcher import fetch_tech_news
from app.services.relevance_checker import get_relevant_news

router = APIRouter()

@router.get("/relevant-news")
def fetch_and_match_news():
    try:
        articles = fetch_tech_news()
        relevant = get_relevant_news(articles)
        return {"status": "success", "articles": relevant}
    except Exception as e:
        return {"status": "error", "message": str(e)}
