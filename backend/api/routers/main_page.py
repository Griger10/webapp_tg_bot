

from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

form_router = APIRouter(tags=["Main page"], route_class=DishkaRoute)

templates = Jinja2Templates(directory="backend/api/templates")


@form_router.get('/')
async def root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "form.html")


@form_router.post('/')
async def process_new_form(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "form_success.html")
