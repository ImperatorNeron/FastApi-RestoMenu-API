from fastapi import APIRouter

from app.presentation.api.v1.categories.handlers import router as category_router


router = APIRouter(prefix="/v1")
router.include_router(router=category_router)
