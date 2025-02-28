from dishka import make_async_container, AsyncContainer

from backend.config.bot_config import get_bot_config
from backend.config.db_config import get_db_config
from backend.config.models import BotConfig, DatabaseConfig
from backend.infrastructure.di.providers import get_providers


def create_container() -> AsyncContainer:
    bot_config = get_bot_config()
    db_config = get_db_config()
    context = {
        BotConfig: bot_config,
        DatabaseConfig: db_config
    }
    container = make_async_container(*get_providers(), context=context)

    return container
