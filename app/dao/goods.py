from app.dao.base import BaseDAO
from app.models.models import Good


class GoodDAO(BaseDAO):
    model = Good