from fastapi import APIRouter
from app.dao.goodsCategory import GoodCategoryDAO
from app.responses.goods import SGoods
from app.models.schemas import goodCategory
from base64 import b64encode
goodsCategoryRouter = APIRouter(prefix="")



@goodsCategoryRouter.get("/goodsCategory/{goodsCategory_id}")
async def get_goodsCategory(goodsCategory_id) -> SGoods | None:
    return await GoodCategoryDAO.find_by_id(int(goodsCategory_id))


@goodsCategoryRouter.post("/goodsCategory")
async def create_goodsCategory(goodsCategory:goodCategory):
    return await GoodCategoryDAO.add(**goodsCategory.dict())

@goodsCategoryRouter.patch("/goodsCategory")
async def patch_goodsCategory(goodsCategory:goodCategory):
    return GoodCategoryDAO.update(goodsCategory.dict(),**goodsCategory.dict())

@goodsCategoryRouter.delete("/goodsCategory")
async def delete_goodsCategory(goodsCategory:goodCategory):
    return GoodCategoryDAO.delete( False,**goodsCategory.dict())