from domain.addresses.use_case_base import AddressUseCaseBase


class DeleteAddressUseCase(AddressUseCaseBase):

    async def execute(self, data):
        await self.repository.delete(data)
