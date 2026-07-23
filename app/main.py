from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
from app.api.user import router as user_router
from app.api.ticket import router as ticket_router
from app.core.config import settings
from app.database.database import Base, engine
from app.models.user import User
from app.models.ticket import Ticket

app = FastAPI(
    title=settings.APP_NAME,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(user_router)
app.include_router(ticket_router)

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Hello, Backend Engineer 👋 How is your day going?"
    }
