import random
from typing import Optional, TypeVar

from aiogram import Bot
from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from backend.api.schemas import CreateForm
from backend.config.models import BotConfig
from backend.infrastructure.db.repositories import UserRepository
from backend.tg_bot.utils.misc import message_admin

form_router = APIRouter(tags=["Main page"], route_class=DishkaRoute, prefix="/forms")


@form_router.get("/")
async def root() -> dict[str, str]:
    return {"message": "Test WebApp bot"}


@form_router.post("/")
async def process_new_form(
    form: CreateForm,
    user_repo: FromDishka[UserRepository],
    bot: FromDishka[Bot],
    bot_config: FromDishka[BotConfig],
) -> dict[str, str | int]:
    await user_repo.update_user_phone_number_and_email(form)
    await message_admin(bot, bot_config, form)
    return {"message": "Message sent", "status_code": HTTP_200_OK}
