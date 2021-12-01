import requests

from domain.entities.address_schemas import AddressObj
from domain.addresses.service_base import ServiceBase


class ViaCepService(ServiceBase):

    def execute(self, data):
        response = requests.get(f"http://viacep.com.br/ws/{data}/json/")
        data = response.json()

        return AddressObj().to_object(data)
