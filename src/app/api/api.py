from fastapi import APIRouter
from .endpoints import test, messages


router = APIRouter()

router.include_router(test.router, prefix="/test", tags=["test"])
router.include_router(messages.router, prefix="/messages", tags=["messages"])


@router.get("/")
async def root():
    return {"message": "HOME"}
