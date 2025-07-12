from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.message import Message
from app.schemas.message import MessageCreate

async def create_message(db: AsyncSession, message_in: MessageCreate):
    db_message = Message(**message_in.dict())
    db.add(db_message)
    await db.commit()
    await db.refresh(db_message)
    return db_message

async def get_messages_by_session(db: AsyncSession, session_id: int):
    result = await db.execute(select(Message).where(Message.session_id == session_id))
    return result.scalars().all()
