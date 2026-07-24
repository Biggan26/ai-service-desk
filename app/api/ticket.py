from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.ticket import TicketCreate, TicketUpdate

from app.database.database import get_db
from app.schemas.ticket import TicketCreate

from app.services.ticket_service import (
    create_ticket,
    get_all_tickets,
    get_ticket_by_id,
    update_ticket,
    delete_ticket,
)

# Groups all ticket-related endpoints under a single router.
router = APIRouter(
    tags=["🎫 Tickets"]
)


# Creates a new ticket
@router.post("/tickets")
def create_new_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):
    return create_ticket(db, ticket)


# Returns
@router.get("/tickets")
def read_tickets(
    db: Session = Depends(get_db)
):
    return get_all_tickets(db)


# Returns a single ticket
@router.get("/tickets/{ticket_id}")
def read_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    return get_ticket_by_id(db, ticket_id)


@router.put("/tickets{ticket_id}")
def update_existing_ticket(
    ticket_id: int,
    ticket: TicketUpdate,
    db: Session = Depends(get_db),
):
    return update_ticket(db, ticket_id, ticket)


@router.delete("/tickets/{ticket_id}")
def delete_existing_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
):
    return delete_ticket(db, ticket_id)
