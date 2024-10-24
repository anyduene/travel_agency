from .base import BaseRepository
from api.models import TransportBooking


class TransportBookingRepository(BaseRepository):
    model = TransportBooking