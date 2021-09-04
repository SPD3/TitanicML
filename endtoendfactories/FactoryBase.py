from abc import ABC, abstractmethod

class FactoryBase (ABC):

    @abstractmethod
    def getDataPreProcessor():
        pass