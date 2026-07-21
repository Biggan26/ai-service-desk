from fastapi import FastAPI

from app.api.user import router as user_router
from app.core.config import settings
from app.database.database import Base, engine
from app.models.user import User

app = FastAPI(title=settings.APP_NAME)

Base.metadata.create_all(bind=engine)

app.include_router(user_router)


@app.get("/")
def root():
    return {
        "message": "Hello, Backend Engineer! What are you doing 😒😒😒😒"
    }
