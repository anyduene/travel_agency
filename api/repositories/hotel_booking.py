from .base import BaseRepository
from api.models import HotelBooking


class HotelBookingRepository(BaseRepository):
    model = HotelBooking