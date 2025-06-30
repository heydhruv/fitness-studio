from datetime import datetime

from pydantic import BaseModel, Field


class FitnessClassBase(BaseModel):
    name: str = Field(max_length=25)
    datetime: datetime
    available_slots: int
    instructor_id: int


class FitnessClassCreate(FitnessClassBase):
    pass


class FitnessClassResponse(FitnessClassBase):
    id: int

    class Config:
        orm_mode = True
