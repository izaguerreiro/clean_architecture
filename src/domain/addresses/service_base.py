from abc import ABC


class ServiceBase(ABC):

    def execute(self, data):
        ...
