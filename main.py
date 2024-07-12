from fastapi import FastAPI
from src.app.api.api import router as api_router
from src.app.depends import init_db, get_telegram_bot
import asyncio
import uvicorn

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    init_db()
    telegram_bot = get_telegram_bot()
    asyncio.create_task(telegram_bot.application.start())

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
