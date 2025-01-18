from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message
from fluentogram import TranslatorRunner

from backend.tg_bot.keyboards.main_menu import set_main_menu
from backend.tg_bot.keyboards.user_keyboards import create_start_keyboard

router = Router()


@router.message(CommandStart())
async def start(message: Message, bot: Bot, i18n: TranslatorRunner):
    await set_main_menu(bot)
    keyboard = create_start_keyboard()
    await message.answer(i18n.start.message(name=message.from_user.first_name), reply_markup=keyboard)
