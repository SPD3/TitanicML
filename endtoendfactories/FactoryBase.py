from abc import ABC, abstractmethod

class FactoryBase (ABC):

    @abstractmethod
    def getDataPreProcessorType():
        pass

    @abstractmethod
    def getModelType():
        pass