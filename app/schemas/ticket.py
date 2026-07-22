#mynote: Schema API Input & Output Define

from pydantic import BaseModel


# This schema defines the data that clients must send when creating a new ticket.
class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str
    assigned_to: str | None = None
    assigned_to_email: str | None = None
