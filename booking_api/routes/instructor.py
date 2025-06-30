import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from booking_api.crud import instructor
from booking_api.db.database import get_db
from booking_api.schemas.instructor import InstructorCreate, InstructorResponse

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/instructors", response_model=InstructorResponse)
def create_instructor(instructor_create: InstructorCreate, db: Session = Depends(get_db)):
    """Creates Instructor Record"""
    created = instructor.create_instructor(db, instructor_create)
    logger.info(f"Instructor created: {created.name} (id={created.id})")
    return created


@router.get("/instructors", response_model=list[InstructorResponse])
def list_instructors(db: Session = Depends(get_db)):
    """Returns List of Instructors"""
    instructors = instructor.get_all_instructors(db)
    logger.info(f"Retrieved {len(instructors)} instructors")
    return instructors
