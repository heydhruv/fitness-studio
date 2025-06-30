import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from booking_api.crud import booking, client
from booking_api.db.database import get_db
from booking_api.schemas.booking import BookingCreate, BookingResponse

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/book", response_model=BookingResponse)
def book_class(booking_create: BookingCreate, db: Session = Depends(get_db)):
    """
    Book a slot in a fitness class for a given client.

    Decrements available slots if booking is successful.
    """
    book = booking.create_booking(db, booking_create)
    logger.info(f"Booking confirmed: booking_id={book.id}")
    if not book:
        raise HTTPException(status_code=400, detail="Booking failed")
    return book


@router.get("/bookings", response_model=list[BookingResponse])
def get_bookings(email: str, db: Session = Depends(get_db)):
    """
    Retrieve all bookings for a client using their email.
    """
    logger.info(f"Fetching bookings for {email}")
    client_booking = client.get_client_by_email(db, email)
    if not client_booking:
        raise HTTPException(status_code=404, detail="Client not found")
    return booking.get_bookings_by_client_id(db, client_booking.id)
