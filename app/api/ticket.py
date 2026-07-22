from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.ticket import TicketCreate
from app.services.ticket_service import (
    create_ticket,
    get_all_tickets,
    get_ticket_by_id,
)

# Groups all ticket-related endpoints under a single router.
router = APIRouter()


# Creates a new ticket using the validated request data.
@router.post("/tickets")
def create_new_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):
    return create_ticket(db, ticket)


# Returns a list of all available tickets.
@router.get("/tickets")
def read_tickets(
    db: Session = Depends(get_db)
):
    return get_all_tickets(db)


# Returns a single ticket by its unique ID.
@router.get("/tickets/{ticket_id}")
def read_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    return get_ticket_by_id(db, ticket_id)
