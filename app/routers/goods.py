from fastapi import APIRouter
from app.dao.goods import GoodDAO
from app.responses.goods import SGoods
from app.models.schemas import good
from base64 import b64encode
goodsRouter = APIRouter(prefix="")



@goodsRouter.get("/goods/{goods_id}")
async def get_goods(goods_id) -> SGoods | None:
    return await GoodDAO.find_by_id(int(goods_id))


@goodsRouter.post("/goods")
async def create_goods(good:good):
    return await GoodDAO.add(**good.dict())

@goodsRouter.patch("/goods")
async def patch_goods(good:good):
    return GoodDAO.update(good.dict(),**good.dict())

@goodsRouter.delete("/goods")
async def delete_goods(good:good):
    return GoodDAO.delete( False,**good.dict())