#store the data in database from Schema validation
#mynote: MODEL Define the structure for Database

from sqlalchemy import Column, Integer, String

from app.database.database import Base


class User(Base):      #database model (USER) that inherit from Base
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
