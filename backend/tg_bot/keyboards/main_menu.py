from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot) -> None:
    commands = [
        BotCommand(command="/start", description="В начало"),
    ]

    await bot.set_my_commands(commands=commands)
