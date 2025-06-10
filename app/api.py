from fastapi import APIRouter
from routers.goods import goodsRouter
from routers.users import usersRouter
from routers.goodsCategories import goodsCategoryRouter
from routers.basket import basketRouter, basketItemsRouter
from auth import authRouter

api = APIRouter(prefix="/api/v1")

api.include_router(goodsRouter)
api.include_router(authRouter)
# api.include_router(usersRouter)
api.include_router(goodsCategoryRouter)
api.include_router(basketRouter)
api.include_router(basketItemsRouter)