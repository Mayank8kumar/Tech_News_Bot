from fastapi import APIRouter
from app.services.news_fetcher import fetch_tech_news

router = APIRouter()

@router.get("/latest-tech-news")
def get_tech_news():
    try:
        news = fetch_tech_news()
        # print("We got the news ##################")
        return {"status": "success", "articles": news}
    except Exception as e:
        return {"status": "error", "message": str(e)}
