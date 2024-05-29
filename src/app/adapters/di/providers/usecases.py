from dishka import Provider, Scope, provide

from app.application.usecases.auth.login_user import LoginUser
from app.application.usecases.auth.register_inactive_user import (
    RegisterInactiveUser,
)
from app.application.usecases.user.users import GetAllUsers


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    get_users = provide(GetAllUsers)

    register_user = provide(RegisterInactiveUser)
    login_user = provide(LoginUser)
