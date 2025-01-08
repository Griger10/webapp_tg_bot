from typing import AsyncIterable

from aiogram import Dispatcher
from dishka import Provider, Scope, provide
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder, Redis


class DispatcherProvider(Provider):
    scope = Scope.APP

    redis = Redis(host='redis', port=6379)

    storage = RedisStorage(
        redis=redis,
        key_builder=DefaultKeyBuilder(with_destiny=True)
    )

    @provide
    async def get_dispatcher(self) -> AsyncIterable[Dispatcher]:
        async with Dispatcher() as dispatcher:
            yield dispatcher
