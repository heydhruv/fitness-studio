from sqlalchemy.orm import Session
from booking_api.schemas.instructor import InstructorCreate
from booking_api.db.models.instructor import Instructor

def create_instructor(db: Session, instructor: InstructorCreate):
    db_instructor = Instructor(name=instructor.name, email=instructor.email)
    db.add(db_instructor)
    db.commit()
    db.refresh(db_instructor)
    return db_instructor

def get_all_instructors(db: Session):
    return db.query(Instructor).all()