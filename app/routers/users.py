from fastapi import APIRouter
from app.dao.users import UserDAO
usersRouter = APIRouter(prefix="/users")



@usersRouter.get("/get_all")
async def get_all_users():
    return await UserDAO.find_all()