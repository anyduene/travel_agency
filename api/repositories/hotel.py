from .base import BaseRepository
from ..models import Hotel


class HotelRepository(BaseRepository):
    model = Hotel
