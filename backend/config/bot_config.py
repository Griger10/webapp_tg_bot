from environs import Env

from backend.config.models import BotConfig


def get_bot_config() -> BotConfig:
    env = Env()
    env.read_env()
    return BotConfig(
        token=env.str("BOT_TOKEN"),
        admin_ids=[int(i) for i in env.list("ADMIN_IDS") if i != ""],
    )
