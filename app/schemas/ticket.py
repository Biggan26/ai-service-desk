# My_note: Schema API Input & Output Define

from pydantic import BaseModel



class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str
    assigned_to: str | None = None
    assigned_to_email: str | None = None


class TicketUpdate(BaseModel):

    title: str
    description: str
    priority: str
    assigned_to: str | None = None
    assigned_to_email: str | None = None
