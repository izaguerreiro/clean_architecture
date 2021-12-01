from domain.addresses.use_case_base import AddressUseCaseBase


class CreateAddressUseCase(AddressUseCaseBase):

    async def execute(self, data):
        await self.repository.save(data.dict())
        return data
