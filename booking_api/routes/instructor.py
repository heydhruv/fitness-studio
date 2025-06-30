from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from booking_api.crud import instructor
from booking_api.db.database import get_db
from booking_api.schemas.instructor import InstructorCreate, InstructorResponse

router = APIRouter()


@router.post("/instructors", response_model=InstructorResponse)
def create_instructor(instructor_create: InstructorCreate, db: Session = Depends(get_db)):
    return instructor.create_instructor(db, instructor_create)


@router.get("/instructors", response_model=list[InstructorResponse])
def list_instructors(db: Session = Depends(get_db)):
    return instructor.get_all_instructors(db)
