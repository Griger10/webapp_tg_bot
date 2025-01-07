from dataclasses import dataclass
from typing import List

from environs import Env


@dataclass
class BotConfig:
    token: str
    admin_ids: List[int]


def get_bot_config() -> BotConfig:
    env = Env()
    env.read_env()
    return BotConfig(
        token=env.str("BOT_TOKEN"),
        admin_ids=[int(i) for i in env.list("ADMIN_IDS") if i != ""],
    )
