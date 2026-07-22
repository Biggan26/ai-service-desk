from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate


# Creates a new ticket using the validated request data and saves it to the database.
def create_ticket(db: Session, ticket: TicketCreate):

    # Converts the incoming schema object into a SQLAlchemy model instance.
    db_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
        assigned_to=ticket.assigned_to,
        assigned_to_email=ticket.assigned_to_email,
    )

    # Adds the new ticket to the current database session.
    db.add(db_ticket)

    # Commits the transaction so the ticket is permanently stored.
    db.commit()

    # Reloads the object to fetch generated values like the ticket ID.
    db.refresh(db_ticket)

    # Returns the saved ticket back to the API layer.
    return db_ticket


# Retrieves every ticket available in the database.
def get_all_tickets(db: Session):
    return db.query(Ticket).all()


# Retrieves a single ticket by its unique ID.
def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()
