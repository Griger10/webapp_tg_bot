from dishka import make_async_container, AsyncContainer

from app.infrastructure.di.providers import get_providers


async def create_container() -> AsyncContainer:
    container = make_async_container(*get_providers())

    return container
