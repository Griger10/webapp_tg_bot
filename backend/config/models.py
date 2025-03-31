from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    dsn: str


@dataclass
class BotConfig:
    token: str
    admin_ids: list[int]
