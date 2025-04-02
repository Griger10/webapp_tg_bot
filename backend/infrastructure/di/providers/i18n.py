from dishka import Provider, Scope, provide
from fluentogram import TranslatorHub, TranslatorRunner

from backend.tg_bot.utils.i18n import create_translator_hub


class TranslatorProvider(Provider):
    scope = Scope.APP

    translator_hub = create_translator_hub()  # хаб с текстами

    @provide
    async def get_hub(self) -> TranslatorHub:
        return self.translator_hub

    @provide
    async def get_translator(self) -> TranslatorRunner:
        return self.translator_hub.get_translator_by_locale(locale="ru")
