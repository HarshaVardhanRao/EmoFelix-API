from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils.jwt import get_current_user
from app.core.database import get_db
from app.schemas.user import UserOut
from app.models.user import User as UserModel

router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("/me", response_model=UserOut)
async def get_profile(current_user: UserModel = Depends(get_current_user)):
    return current_user
