from fastapi import APIRouter

from api.schemas import PingResponse
from api.v1.categories.handler import router as category_router


router = APIRouter(prefix="/api")

router.include_router(router=category_router)


@router.get("/ping", response_model=PingResponse)
def ping():
    return PingResponse(result=True)
