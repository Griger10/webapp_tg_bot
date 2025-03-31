from collections.abc import AsyncIterable

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from dishka import Provider, Scope, provide

from backend.config.models import BotConfig


class BotProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_bot(self, bot_config: BotConfig) -> AsyncIterable[Bot]:
        async with Bot(
                token=bot_config.token,
                default=DefaultBotProperties(
                    parse_mode="HTML",
                )
        ) as bot:
            yield bot
