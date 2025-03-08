from aiogram import Router, Bot, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from dishka import FromDishka
from fluentogram import TranslatorRunner

from backend.infrastructure.db.repositories import UserRepository
from backend.tg_bot.fsm.states import StartFSM
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


@router.callback_query(F.data == "start_work")
async def process_start_work(
    callback: CallbackQuery, dialog_manager: DialogManager
) -> None:
    await dialog_manager.start(StartFSM.share_phone)
    await callback.answer()
