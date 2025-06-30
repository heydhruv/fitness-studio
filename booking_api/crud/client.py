from sqlalchemy.orm import Session
from booking_api.schemas.client import ClientCreate
from booking_api.db.models.client import Client


def create_client(db: Session, client_create: ClientCreate):
    db_client = Client(name=client_create.name, email=client_create.email)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_client_by_email(db: Session, email: str):
    return db.query(Client).filter(Client.email == email).first()