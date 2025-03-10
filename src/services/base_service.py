from ..repositories.base_repository import AbstractRepository
from ..repositories.sqlalchemy_repository import ModelType
from ..schemas.base_schema import PyModel


class BaseService:

    def __init__(self, repository: AbstractRepository) -> None:
        self.repository: AbstractRepository = repository

    async def create(self, model: PyModel) -> ModelType:
        return await self.repository.create(data=model.model_dump())

    async def update(self, pk: str, model: PyModel) -> ModelType:
        return await self.repository.update(data=model.model_dump(), id=pk)

    async def delete(self, pk: str) -> None:
        await self.repository.delete(id=pk)

    async def get(self, pk: str) -> ModelType:
        return await self.repository.get_single(id=pk)
