from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from app.notifications.router import router as notifications_router
from app.tasks.task import celery_app


app = FastAPI()  # uvicorn app.main:app --reload

app.include_router(notifications_router)

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

    i = celery_app.control.inspect()
    workers = i.ping()
    if not workers:
        print("Celery не отвечает!")







