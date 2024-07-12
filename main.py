from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.app.api.api import router as api_router
from src.app.depends import init_db, get_telegram_bot
import asyncio
import uvicorn

app = FastAPI()

telegram_bot = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global telegram_bot
    init_db()

    telegram_bot = get_telegram_bot()
    await telegram_bot.initialize()
    task = asyncio.create_task(telegram_bot.start())

    yield

    await telegram_bot.application.stop()
    task.cancel()


app.router.lifespan_context = lifespan

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
