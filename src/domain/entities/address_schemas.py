from __future__ import annotations

from pydantic import BaseModel
from typing import Optional


class AddressInput(BaseModel):
    cep: str
    logradouro: str
    complemento: Optional[str] = None
    bairro: str
    localidade: str
    uf: str
    ddd: int


class AddressOutput(BaseModel):
    cep: str
    logradouro: str
    complemento: Optional[str] = None
    bairro: str
    localidade: str
    uf: str


class AddressObj(BaseModel):
    cep: str
    logradouro: str
    complemento: str
    bairro: str
    localidade: str
    uf: str
    ddd: int

    def to_object(data):
        return AddressObj(
            cep=data["cep"],
            logradouro=data["logradouro"],
            complemento=data["complemento"],
            bairro=data["bairro"],
            localidade=data["localidade"],
            uf=data["uf"],
            ddd=data["ddd"]
        )
