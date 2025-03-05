from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message
from dishka import FromDishka
from fluentogram import TranslatorRunner

from backend.infrastructure.db.repositories import UserRepository
from backend.tg_bot.keyboards.main_menu import set_main_menu
from backend.tg_bot.keyboards.user_keyboards import create_start_keyboard

router = Router()


@router.message(CommandStart())
async def start(
    message: Message,
    bot: Bot,
    i18n: TranslatorRunner,
    user_repo: FromDishka[UserRepository],
) -> None:
    await set_main_menu(bot)
    keyboard = create_start_keyboard()
    await user_repo.insert_user(
        tid=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    await message.answer(
        i18n.start.message(name=message.from_user.first_name), reply_markup=keyboard
    )
