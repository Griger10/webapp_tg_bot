from typing import List, TypeVar

from dishka import Provider

from backend.infrastructure.di.providers.bot import BotProvider
from backend.infrastructure.di.providers.config import ConfigProvider

from backend.infrastructure.di.providers.db import SessionProvider
from backend.infrastructure.di.providers.user import UserRepositoryProvider


def get_providers() -> list[Provider]:
    return [
        BotProvider(),
        SessionProvider(),
        ConfigProvider(),
        UserRepositoryProvider(),
    ]
