import sys

import uvicorn
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from backend.api.common.misc import lifespan
from backend.api.routers.main_page import form_router
from backend.infrastructure.di.ioc import create_container

logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{message}</level>",
    level="INFO",
)

app = FastAPI(
    lifespan=lifespan,
    title="Example API form",
    version="1.0.0",
    root_path="/api",
    openapi_url="/openapi.json",
)

app.include_router(form_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

container = create_container()

setup_dishka(app=app, container=container)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
