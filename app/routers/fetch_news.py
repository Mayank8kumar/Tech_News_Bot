from fastapi import APIRouter
from app.services.news_fetcher import fetch_latest_tech_news

router = APIRouter()

@router.get("/latest-tech-news")
def get_tech_news():
    try:
        news = fetch_latest_tech_news()
        return {"articles": news}
    except Exception as e:
        return {"error": str(e)}
