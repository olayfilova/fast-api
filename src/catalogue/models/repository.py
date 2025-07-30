from src.catalogue.models.sqlalchemy import ProductModel
from src.common.repository.sqlalchemy_repo import BaseSqlAlchemyReository
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from src.common.databases.postgres import get_session


class ProductRepository(BaseSqlAlchemyReository[Product, ProductModel]):
    def __init__(self, session, AsyncSession):
        super().__init__(model=Product, pydantic_model=ProductModel,session=session, async_session=AsyncSession)


def get_product_repository(session: AsyncSession= Depends(get_session), settings=None):
    if settings.DB_ENGINE == "postgresql":
        return ProductRepository(session=session)
    elif settings.DB_ENGINE == "sqlite":
        return ProductRepository(session=session)
    else:
        raise ValueError("Invalid database engine")
    return ProductRepository(session=session)