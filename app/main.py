from fastapi import FastAPI
from app.routers import upload, fetch_news, ask_bot, relevance, analyzer

app = FastAPI()

app.include_router(upload.router)

app.include_router(fetch_news.router)

app.include_router(relevance.router)

app.include_router(ask_bot.router)

app.include_router(analyzer.router)

