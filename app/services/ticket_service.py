from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketUpdate



def create_ticket(db: Session, ticket: TicketCreate):


    db_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
        assigned_to=ticket.assigned_to,
        assigned_to_email=ticket.assigned_to_email,
    )

    db.add(db_ticket)


    db.commit()


    db.refresh(db_ticket)


    return db_ticket



def get_all_tickets(db: Session):
    return db.query(Ticket).all()



def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()




#CURD Operation update ticket
def update_ticket(db: Session, ticket_id: int, ticket_data: TicketUpdate):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket is None:
        return None
    ticket.title = ticket_data.title
    ticket.description = ticket_data.description
    ticket.priority = ticket_data.priority
    ticket.assigned_to = ticket_data.assigned_to
    ticket.assigned_to_email = ticket_data.assigned_to_email
    db.commit()
    db.refresh(ticket)
    return ticket


# Deletes a ticket
def delete_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not db_ticket:
        return None
    db.delete(db_ticket)
    db.commit()
    return db_ticket
