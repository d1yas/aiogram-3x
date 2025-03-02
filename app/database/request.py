from app.database.models import async_session
from app.database.models import User, Category, Item
from sqlalchemy import select, update, delete


async def set_users(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id==tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()



