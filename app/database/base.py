from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request


async def get_db(request: Request) -> AsyncSession:
    async_session = request.app.state.session_maker
    async with async_session() as session:
        yield session
