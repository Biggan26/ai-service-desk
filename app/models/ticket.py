from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Ticket(Base):

    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    description = Column(String(500), nullable=False)


    priority = Column(String(20), nullable=False)


    status = Column(String(20), default="open")


    assigned_to = Column(String(100), nullable=True)


    assigned_to_email = Column(String(255), nullable=True)
