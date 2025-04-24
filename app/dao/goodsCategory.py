from app.dao.base import BaseDAO
from app.models.models import GoodCategory


class GoodCategoryDAO(BaseDAO):
    model = GoodCategory