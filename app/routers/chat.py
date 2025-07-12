from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.services.ai_service import generate_emotional_response
from app.services.message_service import create_message, get_messages_by_session
from app.schemas.message import MessageCreate, MessageOut
from app.utils.jwt import get_current_user
from app.core.database import get_db
from app.models.session import Session as SessionModel
from app.models.user import User as UserModel
from sqlalchemy.future import select

router = APIRouter(prefix="/api/chat", tags=["chat"])

# Send a message in a session
@router.post("/send", response_model=MessageOut)
async def send_message(
    message_in: MessageCreate,
    db: AsyncSession = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    # Optionally check session ownership
    return await create_message(db, message_in)

# Get all messages in a session
@router.get("/messages/{session_id}", response_model=List[MessageOut])
async def get_session_messages(
    session_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    return await get_messages_by_session(db, session_id)

# Start a new chat session
@router.post("/session/start")
async def start_session(
    db: AsyncSession = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    from app.models.session import Session
    new_session = Session(user_id=current_user.id)
    db.add(new_session)
    await db.commit()
    await db.refresh(new_session)
    return {"session_id": new_session.id, "status": new_session.status}

# End a chat session
@router.post("/session/end/{session_id}")
async def end_session(
    session_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    result = await db.execute(select(SessionModel).where(SessionModel.id == session_id, SessionModel.user_id == current_user.id))
    session = result.scalars().first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    session.status = "ended"
    await db.commit()
    return {"session_id": session.id, "status": session.status}

# Async streaming AI response
@router.post("/stream")
async def stream_response(
    message: str,
    current_user: UserModel = Depends(get_current_user)
):
    async def event_stream():
        async for chunk in generate_emotional_response(message):
            yield chunk
    return StreamingResponse(event_stream(), media_type="text/plain")
