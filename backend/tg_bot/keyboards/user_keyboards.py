from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_start_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Начать работу", callback_data="start_work"),
            ]
        ]
    )
