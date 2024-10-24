from .base import BaseRepository
from ..models import Payment

class PaymentRepository(BaseRepository):
    model = Payment