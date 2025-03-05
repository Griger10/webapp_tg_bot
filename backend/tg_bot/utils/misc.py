from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine


async def test_engine(engine: AsyncEngine) -> None:
    async with engine.begin() as connection:
        await connection.execute(text('SELECT 1'))
