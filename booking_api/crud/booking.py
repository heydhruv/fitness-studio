from datetime import datetime, timezone
from sqlite3 import IntegrityError

from fastapi import HTTPException
from sqlalchemy.orm import Session

from booking_api.db.models.booking import Booking
from booking_api.db.models.fitness_class import FitnessClass
from booking_api.schemas.booking import BookingCreate


def create_booking(db: Session, booking: BookingCreate):
    now_utc = datetime.now(timezone.utc)
    fitness_class = (
        db.query(FitnessClass)
        .filter(
            FitnessClass.id == booking.class_id,
            FitnessClass.datetime >= now_utc
        )
        .with_for_update()
        .first()
    )
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")
    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    existing_booking = db.query(Booking).filter(
        Booking.class_id == booking.class_id,
        Booking.client_id == booking.client_id
    ).first()

    if existing_booking:
        raise HTTPException(
            status_code=409, detail="Client already booked this class.")

    try:

        db_booking = Booking(**booking.model_dump())
        db.add(db_booking)

        fitness_class.available_slots -= 1

        db.commit()
        db.refresh(db_booking)
        return db_booking
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=500, detail="Booking failed due to integrity error")


def get_bookings_by_client_id(db: Session, client_id: int):
    return db.query(Booking).filter(Booking.client_id == client_id).all()
