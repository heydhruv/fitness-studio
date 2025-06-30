from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from booking_api.db.database import Base


class FitnessClass(Base):
    __tablename__ = "fitness_classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    datetime = Column(DateTime(timezone=True), nullable=False)
    available_slots = Column(Integer, nullable=False, default=20)
    instructor_id = Column(Integer, ForeignKey(
        "instructors.id"), nullable=False)
