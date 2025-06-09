from fastapi import APIRouter
from app.dao.users import UserDAO
from app.models.schemas import user
usersRouter = APIRouter(prefix="")



@usersRouter.get("/users/{users_id}")
async def get_goodsCategory(users_id):
    return await UserDAO.find_by_id(int(users_id))


@usersRouter.post("/users")
async def create_goodsCategory(user:user):
    return await UserDAO.add(**user.dict())

@usersRouter.patch("/users")
async def patch_goodsCategory(user:user):
    return UserDAO.update(user.dict(),**user.dict())

@usersRouter.delete("/users")
async def delete_goodsCategory(user:user):
    return UserDAO.delete( False,**user.dict())