from app.dao.base import BaseDAO
from app.models.models import BasketItem


class BasketItemDAO(BaseDAO):
    model = BasketItem