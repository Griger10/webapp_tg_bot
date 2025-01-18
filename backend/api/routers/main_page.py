from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

form_router = APIRouter(tags=["Main page"], route_class=DishkaRoute)


@form_router.get('/')
async def root():
    return {'message': 'Hello World'}


@form_router.post('/')
async def process_new_form():
    return {'form_success': True}
