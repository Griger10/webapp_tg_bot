import uvicorn
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from backend.api.common.misc import lifespan
from backend.api.routers.main_page import form_router
from backend.infrastructure.di.ioc import create_container

app = FastAPI(lifespan=lifespan)

app.include_router(form_router)

container = create_container()

setup_dishka(app=app, container=container)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
