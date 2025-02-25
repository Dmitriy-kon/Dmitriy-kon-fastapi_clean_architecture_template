from fastapi import APIRouter

from app.presentation.web_api.routers.auth import auth_router
from app.presentation.web_api.routers.health_check import health_check_router
from app.presentation.web_api.routers.user import user_router

root_router = APIRouter()
root_router.include_router(health_check_router)

root_router.include_router(user_router)
root_router.include_router(auth_router)

