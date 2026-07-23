# My_note: Schema API Input & Output Define

from pydantic import BaseModel, Field



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



#from Souvav vai Code:  Copy pase from ms TEAm
class SummarizeRequest(BaseModel):
    ticket_description: str = Field(min_length=10, max_length=5_000)


class SummarizeResponse(BaseModel):
    summary: str
    suggested_response: str
