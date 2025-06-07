from fastapi import APIRouter
from app.dao.users import UserDAO
from app.responses.goods import SGoods
from app.models.schemas import user
from base64 import b64encode
usersRouter = APIRouter(prefix="")



@usersRouter.get("/users/{users_id}")
async def get_goodsCategory(users_id) -> SGoods | None:
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