from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator


def create_translator_hub() -> TranslatorHub:
    """Возвращает хаб с корневой локалью ru"""
    translator_hub = TranslatorHub(
        {"ru": "ru"},
        [
            FluentTranslator(
                locale="ru",
                translator=FluentBundle.from_files(
                    locale="ru-RU",
                    filenames=[
                        "backend/tg_bot/locales/ru/LC_MESSAGES/txt.ftl",
                    ],
                ),
            ),
        ],
        root_locale="ru",
    )
    return translator_hub
