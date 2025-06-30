from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from booking_api.crud import booking, client
from booking_api.db.database import get_db
from booking_api.schemas.booking import BookingCreate, BookingResponse

router = APIRouter()


@router.post("/book", response_model=BookingResponse)
def book_class(booking_create: BookingCreate, db: Session = Depends(get_db)):
    book = booking.create_booking(db, booking_create)
    if not book:
        raise HTTPException(status_code=400, detail="Booking failed")
    return book


@router.get("/bookings", response_model=list[BookingResponse])
def get_bookings(email: str, db: Session = Depends(get_db)):
    client_booking = client.get_client_by_email(db, email)
    if not client_booking:
        raise HTTPException(status_code=404, detail="Client not found")
    return booking.get_bookings_by_client_id(db, client_booking.id)
