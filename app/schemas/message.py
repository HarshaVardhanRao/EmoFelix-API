from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MessageBase(BaseModel):
    session_id: int
    sender: str
    content: str
    emotion: Optional[str] = None

class MessageCreate(MessageBase):
    pass

class MessageOut(MessageBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
