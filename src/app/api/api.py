from fastapi import APIRouter
from .endpoints import test


router = APIRouter()

router.include_router(test.router, prefix="/test", tags=["test"])


@router.get("/")
async def root():
    return {"message": "HOME"}
