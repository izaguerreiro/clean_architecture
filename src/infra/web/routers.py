from fastapi import APIRouter, Path, status, Query
from typing import Any, List, Optional

from domain.addresses.create_address_use_case import CreateAddressUseCase
from domain.addresses.delete_address_use_case import DeleteAddressUseCase
from domain.addresses.update_address_use_case import UpdateAddressUseCase
from domain.addresses.search_address_use_case import SearchAddressUseCase
from domain.addresses.search_address_by_cep_use_case import (
    SearchAddressByCepUseCase
)
from domain.entities.address_schemas import AddressInput, AddressOutput
from infra.repositories.address_repository import AddressRepository
from infra.services.via_cep_service import ViaCepService


router = APIRouter()


@router.get(
    "/address",
    response_model=List[AddressOutput],
    response_model_exclude_unset=True
)
async def search_addresses(
    uf: Optional[str] = Query(None, max_length=2, min_length=2)
):
    return await SearchAddressUseCase(
        respository=AddressRepository()
    ).execute(data=uf)


@router.get("/address/{cep}", response_model=AddressOutput)
async def search_address_by_cep(
    cep: str = Path(default=Any, max_length=9, min_length=9)
):
    return await SearchAddressByCepUseCase(
        respository=AddressRepository(), service=ViaCepService()
    ).execute(data=cep)


@router.post("/address", response_model=AddressOutput, status_code=201)
async def create_address(address: AddressInput):
    await CreateAddressUseCase(
        respository=AddressRepository()
    ).execute(data=address.dict())
    
    return address


@router.put("/address/{cep}", status_code=status.HTTP_204_NO_CONTENT)
async def update_address(cep: str, address: AddressInput):
    await UpdateAddressUseCase(
        respository=AddressRepository()
    ).execute(data=address, cep=cep)


@router.delete("/address/{cep}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(cep: str):
    await DeleteAddressUseCase(
        respository=AddressRepository()
    ).execute(data=cep)
