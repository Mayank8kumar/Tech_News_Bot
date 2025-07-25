from app.services.news_fetcher import fetch_tech_news
from app.services.domain_classifier import classify_domains_from_resume
from google.generativeai import GenerativeModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = GenerativeModel("gemini-2.5-flash")

def analyze_news_relevance():
    articles = fetch_tech_news()
    print("Fetched Articles:", articles)
    domains = classify_domains_from_resume()

    results = []

    for article in articles:
        title = article.get("title", "")
        description = article.get("description", "")
        content = f"{title}. {description}"

        prompt = f"""
        You are a tech assistant. Analyze how this news is relevant to the following user domains: {domains}.

        News: "{content}"

        Give a short relevance score (0 to 10) and a 2-line reason why it may impact the user’s domain or interests.

        Respond in this JSON format: 
        {{
            "title": "...",
            "relevance_score": ...,
            "reason": "..."
        }}
        """

        try:
            response = model.generate_content(prompt)
            results.append(response.text.strip())
        except Exception as e:
            results.append({
                "title": title,
                "relevance_score": 0,
                "reason": f"Error: {str(e)}"
            })

    return results
