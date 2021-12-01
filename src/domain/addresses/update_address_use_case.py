from domain.addresses.use_case_base import AddressUseCaseBase


class UpdateAddressUseCase(AddressUseCaseBase):

    async def execute(self, data, **kwargs):
        old_address = self.repository.search_one(kwargs.get("cep"))
        update_address = {"$set": data.dict()}
        self.repository.update(old_address, update_address)
