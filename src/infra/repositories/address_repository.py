from domain.entities.address_schemas import AddressObj
from infra.database.mongodb import get_database_instance
from domain.addresses.repository_base import RepositoryBase


class AddressRepository(RepositoryBase):

    database = get_database_instance()

    async def save(self, **kwargs):
        self.database.save(kwargs)

    async def delete(self, data):
        self.database.delete_many({"cep": data})

    async def update(self, old_data, new_data):
        self.database.update_one(old_data, new_data)

    async def search(self, data=None):
        if data:
            return list(self.database.find({"uf": data}))

        return list(self.database.find({}))

    async def search_one(self, data):
        address = self.database.find_one({"cep": data})
        if address:
            return AddressObj.to_object(data=address)
