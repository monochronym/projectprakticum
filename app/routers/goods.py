from fastapi import APIRouter
from app.dao.goods import GoodDAO
from app.responses.goods import SGoods
from app.models.schemas import good
goodsRouter = APIRouter(prefix="")



@goodsRouter.get("/goods/{goods_id}")
async def get_goods(goods_id):
    return await GoodDAO.find_by_id(goods_id)

@goodsRouter.get("/goods/")
async def get_all_goods():
    return await GoodDAO.find_all()
@goodsRouter.get("/goods/")
async def get_goods_by_filter(goods_category_id:int):
    if goods_category_id > 0:

        return await GoodDAO.find_by_filter(categoryId=goods_category_id)

    else:
        return await GoodDAO.find_all()


@goodsRouter.post("/goods")
async def create_goods(good:good):
    return await GoodDAO.add(**good.dict())

@goodsRouter.patch("/goods")
async def patch_goods(good:good):
    return GoodDAO.update(good.dict(),**good.dict())

@goodsRouter.delete("/goods")
async def delete_goods(good:good):
    return GoodDAO.delete( False,**good.dict())