from fastapi import HTTPException
from sqlalchemy.orm import Session

from booking_api.db.models.fitness_class import FitnessClass
from booking_api.db.models.instructor import Instructor
from booking_api.schemas.fitness_class import FitnessClassCreate


def create_class(db: Session, class_data: FitnessClassCreate):
    instructor = db.query(Instructor).filter(
        Instructor.id == class_data.instructor_id).first()
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    db_class = FitnessClass(**class_data.model_dump())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class


def get_all_classes(db: Session):
    return db.query(FitnessClass).all()


def get_class_by_id(db: Session, class_id: int):
    return db.query(FitnessClass).filter(FitnessClass.id == class_id).first()
