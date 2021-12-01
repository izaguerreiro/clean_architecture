from abc import ABC, abstractmethod


class RepositoryBase(ABC):

    @abstractmethod
    async def save(self, **kwargs):
        ...

    @abstractmethod
    async def delete(self, data):
        ...

    @abstractmethod
    async def update(self, old_data, new_data):
        ...

    @abstractmethod
    async def search_one(self, data):
        ...

    @abstractmethod
    async def search(self, data):
        ...
