from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.app.api.api import router as api_router
from src.app.depends import telegram_bot
import asyncio
import uvicorn

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await telegram_bot.initialize()
    task = asyncio.create_task(telegram_bot.start())

    yield

    await telegram_bot.stop()
    task.cancel()

app.router.lifespan_context = lifespan
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
