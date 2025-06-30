from pydantic import BaseModel


class BookingBase(BaseModel):
    class_id: int
    client_id: int


class BookingCreate(BookingBase):
    pass


class BookingResponse(BookingBase):
    id: int

    class Config:
        orm_mode = True
