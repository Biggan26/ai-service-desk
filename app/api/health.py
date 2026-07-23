from fastapi import APIRouter
from sqlalchemy import text

from app.database.database import engine

router = APIRouter(tags=["Health"])


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.get("/ready")
def ready():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "ready",
            "database": "connected"
        }

    except Exception:
        return {
            "status": "not ready",
            "database": "disconnected"
        }
