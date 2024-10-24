from .base import BaseRepository
from api.models import Booking


class BookingRepository(BaseRepository):
    model = Booking