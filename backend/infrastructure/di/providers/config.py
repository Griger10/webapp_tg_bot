from dishka import Provider, Scope, from_context, provide

from backend.config.models import DatabaseConfig, BotConfig


class ConfigProvider(Provider):
    scope = Scope.APP

    bot_config = from_context(provides=BotConfig, scope=Scope.APP)

    db_config = from_context(provides=DatabaseConfig, scope=Scope.APP)

    @provide
    async def get_bot_config(self, config: BotConfig) -> BotConfig:
        return config

    @provide
    async def get_db_config(self, config: DatabaseConfig) -> DatabaseConfig:
        return config
