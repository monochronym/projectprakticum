from datetime import datetime
from typing import Annotated

from sqlalchemy import func, LargeBinary
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from uuid import UUID

# from config import get_db_url

DB_HOST="yamanote.proxy.rlwy.net"
DB_PORT=11899
DB_NAME="railway"
DB_USER="postgres"
DB_PASSWORD="JRRdKuAWPEBvkNIKINWVcfplCTpwMYBv"

# DB_HOST='localhost'
# DB_PORT=5433
# DB_NAME='ProjectPrakticum'
# DB_USER='postgres'
# DB_PASSWORD='CasperTo360Flip'



DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# настройка аннотаций
int_pk = Annotated[int, mapped_column(primary_key=True)]
uuid_pk = Annotated[UUID, mapped_column(primary_key=True)]
str_pk = Annotated[str, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_null_true = Annotated[str, mapped_column(nullable=True)]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
