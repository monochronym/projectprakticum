from app.dao.base import BaseDAO
from app.models.models import User


class UserDAO(BaseDAO):
    model = User