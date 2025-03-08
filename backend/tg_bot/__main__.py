import asyncio
import sys

from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs
from dishka.integrations.aiogram import setup_dishka
from aiogram.fsm.storage.redis import Redis, RedisStorage, DefaultKeyBuilder  # type: ignore
from loguru import logger

from backend.config.bot_config import get_bot_config
from backend.infrastructure.di.ioc import create_container
from backend.tg_bot.bot_dialogs.main.dialogs import start_dialog
from backend.tg_bot.handlers import user_handlers, admin_handlers
from backend.tg_bot.middlewares.i18n import TranslatorRunnerMiddleware
from backend.tg_bot.utils.i18n import create_translator_hub

logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{message}</level>",
    level="INFO",
)


@logger.catch
async def main() -> None:
    bot_config = get_bot_config()

    redis = Redis(host="redis", port=6379)

    storage = RedisStorage(
        redis=redis, key_builder=DefaultKeyBuilder(with_destiny=True)
    )

    container = create_container()

    translator_hub = create_translator_hub()

    bot = await container.get(Bot)
    dp = Dispatcher(storage=storage, admin_ids=bot_config.admin_ids)

    setup_dishka(router=dp, container=container, auto_inject=True)

    dp.include_routers(admin_handlers.router, user_handlers.router, start_dialog)

    dp.update.middleware(TranslatorRunnerMiddleware())

    setup_dialogs(dp)

    logger.info("Starting bot")
    await dp.start_polling(bot, _translator_hub=translator_hub)


if __name__ == "__main__":
    asyncio.run(main())
