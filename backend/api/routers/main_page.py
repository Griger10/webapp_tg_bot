from aiogram import Bot
from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from backend.api.schemas import CreateForm
from backend.infrastructure.db.repositories import HolderRepository

form_router = APIRouter(tags=["Main page"], route_class=DishkaRoute)


@form_router.get('/')
async def root():
    return {'message': 'Hello World'}


@form_router.post('/')
async def process_new_form(
        form: CreateForm,
        holder: FromDishka[HolderRepository],
        bot: FromDishka[Bot]
):
    await holder.user.update_user_phone_number_and_email(form)
    return {'message': "Message sent", "status_code": HTTP_200_OK}
