import random
from textwrap import dedent

from aiogram import Bot
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine

from backend.api.schemas import CreateForm
from backend.config.models import BotConfig


async def test_engine(engine: AsyncEngine) -> None:
    async with engine.begin() as connection:
        await connection.execute(text("SELECT 1"))


async def message_admin(bot: Bot, bot_config: BotConfig, form: CreateForm) -> None:
    template = dedent(
        """<b><u>Вам поступила новая заявка!</u></b>
        <b>Имя:</b> {first_name}
        <b>Фамилия:</b> {last_name}
        <b>Телефон:</b> {phone_number}
        <b>Почта:</b> {email}
    """
    )
    await bot.send_message(
        chat_id=random.choice(bot_config.admin_ids),
        text=template.format(**form.model_dump()),
    )
