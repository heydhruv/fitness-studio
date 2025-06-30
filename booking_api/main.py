from fastapi import FastAPI

from booking_api.db.database import Base, engine
from booking_api.routes import booking, client, fitness_class, instructor

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fitness Studio Booking API")

app.include_router(fitness_class.router)
app.include_router(client.router)
app.include_router(instructor.router)
app.include_router(booking.router)
