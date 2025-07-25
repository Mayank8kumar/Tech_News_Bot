# Tech Relevance AI

**Tech Relevance AI** is a personalized AI system that analyzes your resume, detects your key tech domains, fetches trending tech news, and intelligently scores how relevant each news article is to your career interests using LLM-based reasoning.

---

##  Project Structure

```
Tech_Relevance_AI/
├── app/
│   ├── faiss_index/                    # FAISS vector DB files
│   ├── routers/                        # FastAPI route handlers
│   │   ├── upload.py                   # Resume upload API
│   │   ├── ask_bot.py                  # Bot for general queries
│   │   ├── fetch_news.py               # Endpoint to fetch news
│   │   ├── relevance.py                # News relevance scoring
│   │   ├── analyzer.py                 # Domain analysis
│   ├── services/                       # Core logic components
│   │   ├── domain_classifier.py        # Gemini-based resume domain classification
│   │   ├── llm_chain.py                # Prompt template and LLM interface
│   │   ├── news_fetcher.py             # Tech news API integration
│   │   ├── relevance_checker.py        # Scores news relevance to user domains
│   │   ├── trend_analyzer.py           # Tech trend prediction logic
│   │   ├── vector_store.py             # FAISS storage and retrieval
│   ├── utils/
│   │   └── extract_text.py            # Extracts the text from file
|   ├── main.py                        # FASTAPI routes calling
|
├── streamlit_app.py                   # Streamlit frontend interface
├── template.py                        # Template for file structure (if applicable)
├── temp_resume.pdf                    # Temporary uploaded resume (hidden from user)
├── .env                               # API keys and config vars
├── requirements.txt                   # Project dependencies
├── README.md                          # This file
```

---

## 🔧 Features

* **Resume Upload:** Upload your resume securely to extract relevant tech domains.
* **Domain Detection:** Uses LLM (Gemini 2.5) to extract AI/ML-relevant domain areas.
* **Tech News Fetcher:** Pulls trending tech news from API.
* **Relevance Scoring:** RAG pipeline with embeddings + LLM to score news relevance.
* **FAISS Vector Store:** Stores user-contextual information for efficient retrieval.
* **Streamlit Frontend:** Interactive UI for resume upload, domain detection, and news scoring.

---

## 📀 Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **LLM Provider:** Google Generative AI (Gemini 2.5)
* **Embeddings:** Google Generative AI Embeddings
* **Vector DB:** FAISS
* **Data Flow:** Resume → Domain Classifier → News Fetch → Relevance Scoring

---

## ⚙️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Mayank8kumar/Tech_News_Bot
   cd tech-relevance-ai
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   env\Scripts\activate                     # or source env/bin/activate on Mac
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up `.env` file**
   Create a `.env` file in the root directory and add:

   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

5. **Run the backend**

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Run the frontend**

   ```bash
   streamlit run streamlit_app.py
   ```

---

## 💡 How It Works

1. **Upload Resume/LinkedIn Profile:** Sent to `/upload-resume`, stored temporarily and used for inference.
2. **Domain Classification:** `/detect-domain` sends resume text to Gemini, which responds with comma-separated domains.
3. **News Fetching:** `/fetch-news` pulls the latest tech news via an API.
4. **Relevance Scoring:** `/relevant-news` uses the resume context + news and scores relevance using a combination of RAG + Gemini LLM.
5. **Frontend:** Built using Streamlit, communicates with all backend endpoints.

---

## 📁 Deployment Notes

* Ensure `temp_resume.pdf` is hidden from the frontend.
* Use production environment variables instead of `.env` for deployment.
* Avoid enabling dangerous deserialization unless the pickle source is trusted.

---

## ✅ To-Do / Upcoming

* [ ] Add news summarization bot.
* [ ] Integrate historical trend insights per domain.
* [ ] Implement caching for repeated users.
* [ ] Add login system for personalized storage.

---

## 👤 Author

**Mayank Kumar**
Backend & AI Developer | Python, FastAPI, LLMs, Streamlit
