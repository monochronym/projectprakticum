from fastapi import APIRouter
from app.dao.goods import GoodDAO
from app.responses.goods import SGoods
from app.models.schemas import Good
goodsRouter = APIRouter(prefix="")



@goodsRouter.get("/goods/{goods_id}")
async def get_goods(goods_id) -> SGoods | None:
    return await GoodDAO.find_by_id(int(goods_id))


@goodsRouter.post("/goods")
async def create_goods(good:Good):
    return await GoodDAO.add(**good.dict())

@goodsRouter.patch("/goods")
async def patch_goods(good:Good):
    return GoodDAO.update(good.dict(),**good.dict())

@goodsRouter.delete("/goods")
async def delete_goods(good:Good):
    return GoodDAO.delete( False,**good.dict())