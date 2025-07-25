from fastapi import FastAPI
from app.routers import upload
from app.routers import fetch_news
from app.routers import relevance
from app.routers import ask_bot

app = FastAPI()

app.include_router(upload.router)

app.include_router(fetch_news.router)

app.include_router(relevance.router)

app.include_router(ask_bot.router)

