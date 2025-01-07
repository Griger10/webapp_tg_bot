from urllib.request import Request

from fastapi import APIRouter
from starlette.responses import HTMLResponse

form_router = APIRouter(prefix="/", tags=["Main page"])


@form_router.get('/')
async def root(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "form.html")


@form_router.post('/')
async def process_new_form(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "form_success.html")
