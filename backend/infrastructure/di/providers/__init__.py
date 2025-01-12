from typing import List

from backend.infrastructure.di.providers.bot import BotProvider

from backend.infrastructure.di.providers.db import SessionProvider, HolderRepositoryProvider


def get_providers() -> List:
    return [
        BotProvider(),
        SessionProvider(),
        HolderRepositoryProvider()
    ]
