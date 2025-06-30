import logging
from zoneinfo import ZoneInfo

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from sqlalchemy.orm import Session

from booking_api.crud import fitness_class
from booking_api.db.database import get_db
from booking_api.schemas.fitness_class import FitnessClassCreate, FitnessClassResponse

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/classes", response_model=list[FitnessClassResponse])
def get_classes(request: Request, db: Session = Depends(get_db)):
    """Retrieve all upcoming fitness classes"""
    results = fitness_class.get_all_classes(db)
    try:
        tz = request.headers.get("x-timezone", "Asia/Kolkata")
        user_tz = ZoneInfo(tz)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid timezone")

    for fc in results:
        fc.datetime = fc.datetime.astimezone(user_tz)
    logger.info(f"Returned {len(results)} classes to user in {tz}")
    return results


@router.post("/classes", response_model=FitnessClassResponse)
def add_class(class_data: FitnessClassCreate, db: Session = Depends(get_db)):
    """Create Fitness Class Record"""
    return fitness_class.create_class(db, class_data)
