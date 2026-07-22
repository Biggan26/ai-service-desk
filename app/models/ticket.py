from sqlalchemy import Column, Integer, String

# Base is inherited so SQLAlchemy can recognize this class as a database table.
from app.database.database import Base


# This model defines the structure of the tickets table in our database.
class Ticket(Base):

    # Specifies the actual table name that will be created in the database.
    __tablename__ = "tickets"

    # Primary key uniquely identifies each ticket, and indexing speeds up ID-based searches.
    id = Column(Integer, primary_key=True, index=True)

    # Stores the short title of the issue reported by the user.
    title = Column(String(200), nullable=False)

    # Stores the detailed explanation of the reported issue.
    description = Column(String(500), nullable=False)

    # Stores the ticket priority such as low, medium, or high.
    priority = Column(String(20), nullable=False)

    # Every new ticket starts with "open" unless another status is explicitly assigned.
    status = Column(String(20), default="open")






    # Stores the name of the engineer currently assigned to handle the ticket.
    assigned_to = Column(String(100), nullable=True)

    # Stores the email address of the engineer currently assigned to handle the ticket.
    assigned_to_email = Column(String(255), nullable=True)


