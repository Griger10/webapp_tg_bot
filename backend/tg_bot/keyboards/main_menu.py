from aiogram import Bot
from aiogram.types import BotCommand
from fluentogram import TranslatorRunner


async def set_main_menu(bot: Bot):
    commands = [
        BotCommand(command='/menu', description='Перейти в главное меню'),
    ]

    await bot.set_my_commands(commands=commands)
