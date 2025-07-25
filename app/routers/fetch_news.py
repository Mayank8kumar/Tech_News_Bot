from fastapi import APIRouter
from app.services.news_fetcher import fetch_tech_news
from app.services.news_fetcher import fetch_tech_news_Gnews

router = APIRouter()

@router.get("/latest-tech-news")
def get_tech_news():
    try:
        news = fetch_tech_news()
        # print("We got the news ##################")
        return {"status": "success", "articles": news}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@router.get("/latest-tech-news-Gnews")
def get_tech_news_Gnews():
    try:
        news = fetch_tech_news_Gnews()
        # print("We got the news ##################")
        return {"status": "success", "articles": news}
    except Exception as e:
        return {"status": "error", "message": str(e)}