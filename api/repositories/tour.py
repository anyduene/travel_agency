from .base import BaseRepository
from ..models import Tour

class TourRepository(BaseRepository):
    model = Tour