from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.payment import Payment
from app.schemas.payment import PaymentCreate

async def create_payment(db: AsyncSession, payment_in: PaymentCreate):
    db_payment = Payment(**payment_in.dict())
    db.add(db_payment)
    await db.commit()
    await db.refresh(db_payment)
    return db_payment

async def get_payments_by_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(Payment).where(Payment.user_id == user_id))
    return result.scalars().all()
