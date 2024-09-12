from fastapi import APIRouter

from app.presentation.api.schemas import PingResponse
from app.presentation.api.v1.handlers import router as v1_router


router = APIRouter(prefix="/api")

router.include_router(router=v1_router)


@router.get("/ping", response_model=PingResponse)
def ping():
    return PingResponse(result=True)
