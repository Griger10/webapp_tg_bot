import asyncio

from fastapi import FastAPI

from app.web.api.common.misc import lifespan
from app.web.api.routers import form_router


async def main():
    app_ = FastAPI(lifespan=lifespan)

    app_.include_router(form_router)


if __name__ == '__main__':
    asyncio.run(main())
