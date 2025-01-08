from environs import Env

from app.config.models import DatabaseConfig


def get_db_config() -> DatabaseConfig:
    env = Env()
    env.read_env()

    return DatabaseConfig(
        dsn=env.str('DATABASE_DSN')
    )
