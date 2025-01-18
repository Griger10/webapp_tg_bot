from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.kbd import Button


async def go_next(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.next()


async def go_back(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.back(show_mode=ShowMode.EDIT)


async def do_nothing(
        callback: CallbackQuery, widget: Button, dialog_manager: DialogManager
):
    await callback.answer()
