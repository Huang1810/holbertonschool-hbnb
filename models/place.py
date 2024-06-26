import uuid
from datetime import datetime
from .base import BaseModel


class Place(BaseModel):
    def __init__(self, name, host, description="", address="", city=None, latitude=0.0, longitude=0.0, 
                 number_of_rooms=0, bathrooms=0, price_per_night=0.0, max_guests=0, amenities=None, reviews=None):
        super().__init__()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.name = name
        self.host = host
        self.bathrooms = bathrooms
        self.city = city
        self.longitude = longitude
        self.latitude = latitude
        self.description = description
        self.number_of_rooms = number_of_rooms
        self.address = address
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = amenities or []
        self.reviews = reviews or []
