from domain.addresses.use_case_base import AddressUseCaseBase


class SearchAddressByCepUseCase(AddressUseCaseBase):

    async def execute(self, data):
        address = await self.repository.search_one(data=data)
        
        if not address:
            address = self.service.execute(data=data)
            await self.repository.save(**address.dict())
        
        return address
