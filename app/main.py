from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.infrastructure.sqlalchemy_orm.database import database_helper
from app.presentation.api.handlers import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await database_helper.dispose()


def create_app() -> FastAPI:
    application = FastAPI(
        title="RestoMenu",
        docs_url="/api/docs",
        description="PetProject using FastApi/Docker/SqlAlchemy/Alembic",
        default_response_class=ORJSONResponse,
        debug=True,
        lifespan=lifespan,
    )
    application.include_router(router=router)

    return application
