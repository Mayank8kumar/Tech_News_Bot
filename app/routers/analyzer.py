from fastapi import APIRouter
from app.services.trend_analyzer import analyze_news_relevance

router = APIRouter()

@router.get("/analyze-news")
def analyze_news():
    return analyze_news_relevance()
