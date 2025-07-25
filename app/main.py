from fastapi import FastAPI
from app.routers import upload
from app.routers import fetch_news

app = FastAPI()

app.include_router(upload.router)

app.include_router(fetch_news.router)
