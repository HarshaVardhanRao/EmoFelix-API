from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PaymentBase(BaseModel):
    amount: float
    status: Optional[str] = "pending"

class PaymentCreate(PaymentBase):
    user_id: int

class PaymentOut(PaymentBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
