from fastapi import FastAPI

from app.api.user import router as user_router
from app.api.ticket import router as ticket_router

from app.core.config import settings

from app.database.database import Base, engine

from app.models.user import User
from app.models.ticket import Ticket


# Creates the FastAPI application using the project name from the configuration.
app = FastAPI(title=settings.APP_NAME)


# Creates all database tables for the registered SQLAlchemy models if they do not already exist.
Base.metadata.create_all(bind=engine)


# Registers all user-related API endpoints with the application.
app.include_router(user_router)

# Registers all ticket-related API endpoints with the application.
app.include_router(ticket_router)


# Provides a simple endpoint to verify that the application is running.
@app.get("/")
def root():
    return {
        "message": "Hello, Backend Engineer ??  What are you doing today 😒😒"
    }
