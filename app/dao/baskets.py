from app.dao.base import BaseDAO
from app.models.models import Basket


class BasketDAO(BaseDAO):
    model = Basket