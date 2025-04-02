import random

from aiogram import Bot
from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject
from fluentogram import TranslatorRunner

from backend.config.models import BotConfig
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


async def topic_handler(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager,
):
    topic = message.text.strip()
    dialog_manager.dialog_data["topic"] = topic
    await dialog_manager.next()


@inject
async def problem_handler(
        message: Message,
        dialog_manager: DialogManager,
        bot: FromDishka[Bot],
        bot_config: FromDishka[BotConfig],
        i18n: TranslatorRunner
):
    problem = message.text.strip()
    topic = dialog_manager.dialog_data["topic"]

    await bot.send_message(
        chat_id=random.choice(bot_config.admin_ids),
        text=i18n.new.ask(
            name=message.from_user.first_name,
            topic=topic,
            problem=problem
        ),
    )
