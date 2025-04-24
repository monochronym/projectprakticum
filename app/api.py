from fastapi import APIRouter
from app.routers.goods import goodsRouter
from app.auth import authRouter

api = APIRouter(prefix="/api/v1")

api.include_router(goodsRouter)
api.include_router(authRouter)