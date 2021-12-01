from domain.addresses.use_case_base import AddressUseCaseBase


class SearchAddressUseCase(AddressUseCaseBase):

    async def execute(self, data=None):
        return list(await self.repository.search(data))
