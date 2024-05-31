from fastapi import FastAPI
from src.app.api.api import router as api_router


app = FastAPI(
    title='TeleCO2gram',
    docs_url='/docs'
)

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
