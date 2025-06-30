from sqlalchemy import Column, ForeignKey, Integer, String

from booking_api.db.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey(
        "fitness_classes.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"))
