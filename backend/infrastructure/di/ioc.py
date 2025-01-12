from dishka import make_async_container, AsyncContainer

from backend.config.bot_config import get_bot_config
from backend.infrastructure.di.providers import get_providers


def create_container() -> AsyncContainer:
    container = make_async_container(*get_providers())

    return container
