from typing import cast

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.types import ExceptionHandler

from app.application.common.exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
    UserPasswordNotMatchError,
)


async def user_allready_exists_handler(
    request: Request, exc: UserAlreadyExistsError
) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"message": exc.message},
    )


async def user_not_found_handler(
    request: Request, exc: UserNotFoundError
) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={"message": exc.message},
    )


async def user_password_not_match_handler(
    request: Request, exc: UserPasswordNotMatchError
) -> JSONResponse:
    return JSONResponse(
        status_code=401,
        content={"message": exc.message},
    )


def init_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        UserAlreadyExistsError, cast(ExceptionHandler, user_allready_exists_handler)
    )
    app.add_exception_handler(
        UserNotFoundError, cast(ExceptionHandler, user_not_found_handler)
    )
    app.add_exception_handler(
        UserPasswordNotMatchError,
        cast(ExceptionHandler, user_password_not_match_handler),
    )
