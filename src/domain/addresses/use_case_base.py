from abc import ABC, abstractmethod
from typing import Any, Optional

from domain.addresses.repository_base import RepositoryBase
from domain.addresses.service_base import ServiceBase


class AddressUseCaseBase(ABC):

    def __init__(
        self,
        respository: RepositoryBase,
        service: Optional[ServiceBase] = None
    ):
        self.repository = respository
        self.service = service

    @abstractmethod
    def execute(self, data: Optional[Any], **kwargs):
        ...
