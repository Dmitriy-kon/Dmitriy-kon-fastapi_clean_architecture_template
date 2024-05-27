from dishka import Provider, Scope, provide

from app.application.usecases.user.users import GetAllUsers
from app.application.usecases.auth.check_user_unique import CheckUserUnique
from app.application.usecases.auth.register_inactive_user import RegisterInactiveUser
from app.application.usecases.auth.login.identificate_user import IdentificateUser
from app.application.usecases.auth.login.authorize_user import AuthorizeUser


class UseCasesProvider(Provider):
    scope = Scope.REQUEST
    
    get_users = provide(GetAllUsers)
    check_user_unique = provide(CheckUserUnique)
    register_user = provide(RegisterInactiveUser)
    
    identificate_user = provide(IdentificateUser)
    authorize_user = provide(AuthorizeUser)