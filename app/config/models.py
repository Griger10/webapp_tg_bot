from dataclasses import dataclass
from typing import List


@dataclass
class DatabaseConfig:
    dsn: str


@dataclass
class BotConfig:
    token: str
    admin_ids: List[int]
