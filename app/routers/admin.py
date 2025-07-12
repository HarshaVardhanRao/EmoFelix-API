from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.database import get_db
from app.models.user import User as UserModel
from app.utils.jwt import get_current_user

router = APIRouter(prefix="/api/admin", tags=["admin"])

@router.get("/users")
async def list_users(
    db: AsyncSession = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    if not current_user.is_admin:
        from fastapi import HTTPException
        raise HTTPException(status_code=403, detail="Not authorized")
    result = await db.execute(select(UserModel))
    return result.scalars().all()
