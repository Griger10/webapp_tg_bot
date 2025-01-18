from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_start_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Пройти регистрацию 📝', callback_data='fill_form'),
            ]
        ]
    )
