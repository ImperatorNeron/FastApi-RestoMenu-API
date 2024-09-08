from fastapi import FastAPI

from api.handler import router


def create_app() -> FastAPI:
    application = FastAPI(
        title="RestoMenu",
        docs_url="/api/docs",
        description="PetProject using FastApi/Docker/SqlAlchemy/Alembic",
        debug=True,
    )
    application.include_router(router=router)

    return application
