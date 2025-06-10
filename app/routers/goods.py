import uuid

from fastapi import APIRouter
from app.dao.goods import GoodDAO
from app.responses.goods import SGoods
from app.models.schemas import good
import base64
goodsRouter = APIRouter(prefix="")
import os

def set_image_to_good(good):
    current_dir = os.path.abspath(os.getcwd())
    with open(os.path.join(current_dir, 'media', str(good['id']) + ".jpg"), 'rb') as file:
        encoded_bytes = base64.b64encode(file.read())
        encoded_str = encoded_bytes.decode('utf-8')
    good["file_bytes"] = encoded_str
    return good
@goodsRouter.get("/goods/{goods_id}")
async def get_goods(goods_id):
    good = await GoodDAO.find_by_id(goods_id)
    ans_good = set_image_to_good({column.name: getattr(good, column.name) for column in good.__table__.columns})
    return ans_good

@goodsRouter.get("/goods/")
async def get_all_goods():
    goods = await GoodDAO.find_all()
    ret_goods = list()
    for good in goods:
        ret_goods.append(set_image_to_good({column.name: getattr(good, column.name) for column in good.__table__.columns}))
    return ret_goods
@goodsRouter.get("/goods/")
async def get_goods_by_filter(goods_category_id:int):
    ret_goods = list()
    if goods_category_id > 0:
        goods = await GoodDAO.find_by_filter(categoryId=goods_category_id)
        for good in goods:
            ret_goods.append(set_image_to_good({column.name: getattr(good, column.name) for column in good.__table__.columns}))
        return goods

    else:
        goods = await GoodDAO.find_all()
        for good in goods:
            ret_goods.append(set_image_to_good({column.name: getattr(good, column.name) for column in good.__table__.columns}))
        return goods


@goodsRouter.post("/goods")
async def create_goods(good:good):
    good.id = uuid.uuid4()
    file_bytes = base64.b64decode(good.file_bytes)
    current_dir = os.path.abspath(os.getcwd())
    with open(os.path.join(current_dir,'media', str(good.id) + ".jpg"), 'wb') as file:
        file.write(file_bytes)
        file.close()
    del good.file_bytes
    return await GoodDAO.add(**good.dict())

@goodsRouter.patch("/goods")
async def patch_goods(good:good):
    return GoodDAO.update(good.dict(),**good.dict())

@goodsRouter.delete("/goods")
async def delete_goods(good:good):
    return GoodDAO.delete( False,**good.dict())