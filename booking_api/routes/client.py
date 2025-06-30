from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from booking_api.crud import client as client_crud
from booking_api.db.database import get_db
from booking_api.schemas.client import ClientCreate, ClientResponse

router = APIRouter()


@router.post("/clients", response_model=ClientResponse)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    existing = client_crud.get_client_by_email(db, client.email)
    if existing:
        raise HTTPException(status_code=409, detail="Client already exists.")
    return client_crud.create_client(db, client)
