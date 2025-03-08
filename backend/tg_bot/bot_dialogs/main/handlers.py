from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from backend.infrastructure.db.repositories.user import IUserRepository


@inject
async def phone_handler(
    message: Message,
    widget: MessageInput,
    dialog_manager: DialogManager,
    user_repo: FromDishka[IUserRepository],
) -> None:
    await user_repo.update_user_phone_number(
        message.from_user.id, message.contact.phone_number  # type: ignore
    )
    await dialog_manager.next()
