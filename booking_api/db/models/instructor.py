from sqlalchemy import Column, ForeignKey, Integer, String

from booking_api.db.database import Base


class Instructor(Base):
    __tablename__ = "instructors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
