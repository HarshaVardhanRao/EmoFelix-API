from fastapi import FastAPI
from app.routers import auth, users, chat, payments, admin

app = FastAPI(title="EmoFelix API", docs_url="/docs")

# All routers use /api prefix
app.include_router(auth.router, prefix="/api")
app.include_router(users.router, prefix="/api")
app.include_router(chat.router)  # already has /api prefix
app.include_router(payments.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
