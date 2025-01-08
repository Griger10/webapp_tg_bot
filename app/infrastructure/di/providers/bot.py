from typing import AsyncIterable

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from dishka import Provider, Scope, provide, from_context

from app.config.models import BotConfig


class BotProvider(Provider):
    scope = Scope.APP

    config = from_context(provides=BotConfig)

    @provide
    async def get_bot(self, config: BotConfig) -> AsyncIterable[Bot]:
        async with Bot(
                token=config.token,
                default=DefaultBotProperties(
                    parse_mode="HTML",
                )
        ) as bot:
            yield bot
