from fastapi import APIRouter
from app.services.vector_store import load_resume_text
from app.services.llm_chain import get_llm_response
from app.services.news_fetcher import fetch_tech_news

router = APIRouter()

@router.get("/explain-relevance")
def explain_relevance():
    try:
        resume_text = load_resume_text()
        articles = fetch_tech_news(page_size=3)  # Limit to 3 for demo
        results = []

        for article in articles:
            title = article.get("title", "")
            description = article.get("description", "")
            content = f"{title}\n\n{description}"
            explanation = get_llm_response(resume_text, content)

            results.append({
                "title": title,
                "description": description,
                "explanation": explanation
            })

        return {"status": "success", "results": results}
    except Exception as e:
        return {"status": "error", "message": str(e)}
