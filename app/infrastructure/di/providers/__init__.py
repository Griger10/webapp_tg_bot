from typing import List

from app.infrastructure.di.providers.bot import BotProvider
from app.infrastructure.di.providers.dispatcher import DispatcherProvider

from app.infrastructure.di.providers.db import SessionProvider


def get_providers() -> List:
    return [
        BotProvider(),
        DispatcherProvider(),
        SessionProvider(),
    ]
