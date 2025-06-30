from pydantic import BaseModel, EmailStr, Field


class InstrctorBase(BaseModel):
    name: str = Field(max_length=25)
    email: EmailStr


class InstructorCreate(InstrctorBase):
    pass


class InstructorResponse(InstrctorBase):
    id: int

    class Config:
        orm_mode = True
