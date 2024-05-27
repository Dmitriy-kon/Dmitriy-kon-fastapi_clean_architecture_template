from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app.adapters.di.main import container_factory

from app.presentation.web_api.routers.health_check import health_check_router
from app.presentation.web_api.routers.user import user_router
from app.presentation.web_api.routers.auth import auth_router
from app.presentation.web_api.routers.root import root_router


def init_di(app: FastAPI) -> None:
    setup_dishka(container_factory(), app)

def init_router(app: FastAPI) -> None:
    # app.include_router(health_check_router)
    # app.include_router(user_router)
    # app.include_router(auth_router)
    app.include_router(root_router)


def create_app() -> FastAPI:
    app = FastAPI()
    
    init_di(app)
    init_router(app)
    return app