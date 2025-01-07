from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    dsn: str


def get_db_config() -> DatabaseConfig:
    env = Env()
    env.read_env()

    return DatabaseConfig(
        dsn=env.str('DATABASE_DSN')
    )
