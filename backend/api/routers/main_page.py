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

K = TypeVar("K", bound=str)
V = TypeVar("V", str, int)

form_router = APIRouter(tags=["Main page"], route_class=DishkaRoute, prefix="/forms")


@form_router.get("/")
async def root() -> dict[K, V]:
    return {"message": "Hello World"}


@form_router.post("/")
async def process_new_form(
    form: CreateForm,
    user_repo: FromDishka[UserRepository],
    bot: FromDishka[Bot],
    bot_config: FromDishka[BotConfig],
) -> dict[K, V]:
    await user_repo.update_user_phone_number_and_email(form)
    await bot.send_message(
        chat_id=random.choice(bot_config.admin_ids), text=f"Новая заявка: {form}"
    )
    return {"message": "Message sent", "status_code": HTTP_200_OK}
