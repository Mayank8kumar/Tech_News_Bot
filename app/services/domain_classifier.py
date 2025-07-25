from google.generativeai import GenerativeModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
from app.services.vector_store import load_resume_text

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def classify_domains_from_resume():
    resume_text = load_resume_text()

    prompt = f"""
        You are an intelligent assistant. Your job is to extract 3-5 relevant technology domains based on the following resume text.

        Instructions:
        - Focus only on tech-related domains or fields.
        - Return only comma-separated keywords (e.g., "AI/ML, Web Development, DevOps").

        Resume Text:
        {resume_text}
"""

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
