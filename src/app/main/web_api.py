from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app.adapters.di.main import container_factory
from app.presentation.web_api.exc_handlers.exc_handlers import init_exception_handlers
from app.presentation.web_api.routers.root import root_router


def init_di(app: FastAPI) -> None:
    setup_dishka(container_factory(), app)


def init_router(app: FastAPI) -> None:
    app.include_router(root_router)


def create_app() -> FastAPI:
    app = FastAPI()

    init_di(app)
    init_router(app)
    init_exception_handlers(app)
    return app
