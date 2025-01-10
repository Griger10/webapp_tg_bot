import asyncio

from aiogram import Bot, Dispatcher
from dishka.integrations.fastapi import setup_dishka
from dishka.integrations.aiogram import setup_dishka as setup_dishka_
from fastapi import FastAPI

from app.infrastructure.di.ioc import create_container
from app.tg_bot.handlers import user_handlers
from app.web.api.common.misc import lifespan
from app.web.api.routers import form_router


async def main():
    app_ = FastAPI(lifespan=lifespan)

    container = await create_container()

    bot = await container.get(Bot)
    dp = await container.get(Dispatcher)

    setup_dishka(app=app_, container=container)
    setup_dishka_(router=dp, container=container)

    dp.include_router(user_handlers.router)

    app_.include_router(form_router)

    try:
        await dp.start_polling(bot)
    finally:
        await container.close()


if __name__ == '__main__':
    asyncio.run(main())
