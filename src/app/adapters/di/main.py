from dishka import AsyncContainer, make_async_container

from app.adapters.di.providers.adapters import InDbProvider, SqlalchemyProvier
from app.adapters.di.providers.usecases import UseCasesProvider


def container_factory() -> AsyncContainer:
    return make_async_container(
        SqlalchemyProvier(),
        UseCasesProvider(),
        InDbProvider(),
    )
