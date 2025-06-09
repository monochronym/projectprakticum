from fastapi import APIRouter
from app.routers.goods import goodsRouter
from app.routers.users import usersRouter
from app.routers.goodsCategories import goodsCategoryRouter
from app.routers.basket import basketRouter, basketItemsRouter
from app.auth import authRouter

api = APIRouter(prefix="/api/v1")

api.include_router(goodsRouter)
api.include_router(authRouter)
# api.include_router(usersRouter)
api.include_router(goodsCategoryRouter)
api.include_router(basketRouter)
api.include_router(basketItemsRouter)