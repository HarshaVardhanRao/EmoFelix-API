from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.payment import PaymentCreate, PaymentOut
from app.services.payment_service import create_payment, get_payments_by_user
from app.utils.jwt import get_current_user
from app.core.database import get_db
from app.models.user import User as UserModel
from typing import List

router = APIRouter(prefix="/api/payments", tags=["payments"])

@router.post("/create", response_model=PaymentOut)
async def create_payment_endpoint(
    payment_in: PaymentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    return await create_payment(db, payment_in)

@router.get("/my", response_model=List[PaymentOut])
async def get_my_payments(
    db: AsyncSession = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    return await get_payments_by_user(db, current_user.id)
