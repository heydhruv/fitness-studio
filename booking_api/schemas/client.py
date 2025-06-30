from pydantic import BaseModel, EmailStr, Field


class ClientBase(BaseModel):
    name: str = Field(max_length=25)
    email: EmailStr


class ClientCreate(ClientBase):
    pass


class ClientResponse(ClientBase):
    id: int

    class Config:
        orm_mode = True
