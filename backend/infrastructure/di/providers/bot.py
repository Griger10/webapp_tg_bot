from typing import AsyncIterable

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from dishka import Provider, Scope, provide

from backend.config.bot_config import get_bot_config
from backend.config.models import BotConfig


class BotProvider(Provider):
    scope = Scope.APP

    config: BotConfig = get_bot_config()

    @provide
    async def get_bot(self) -> AsyncIterable[Bot]:
        async with Bot(
                token=self.config.token,
                default=DefaultBotProperties(
                    parse_mode="HTML",
                )
        ) as bot:
            yield bot
