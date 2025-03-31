
from environs import Env

from backend.config.models import BotConfig


def get_bot_config() -> BotConfig:
    env = Env()
    env.read_env()
    admin_ids: list[str] = env.list("ADMIN_IDS")
    return BotConfig(
        token=env.str("BOT_TOKEN"),
        admin_ids=[int(i) for i in admin_ids if i != ""],
    )
