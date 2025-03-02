from app.database.models import async_session
from app.database.models import User, Category, Item
from sqlalchemy import select, update, delete


async def set_users(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id==tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()



async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))

async def get_category_item(category_id):
    async with async_session() as session:
        return await session.scalars(select(Item).where(Item.category == category_id))


async def get_item_category(item_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.id == item_id))
