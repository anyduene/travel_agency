from .base import BaseRepository
from ..models import Client

class ClientRepository(BaseRepository):
    model = Client