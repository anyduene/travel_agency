from .base import BaseRepository
from api.models import Transport

class TransportRepository(BaseRepository):
    model = Transport