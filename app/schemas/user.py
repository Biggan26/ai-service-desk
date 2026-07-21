#take input from user and validate it using pydantic
#pydantic is used to validate the data before storing it in the database


from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
