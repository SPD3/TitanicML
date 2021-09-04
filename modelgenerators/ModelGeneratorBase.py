from abc import ABC, abstractmethod

class ModelGeneratorBase (ABC):

    @abstractmethod
    def createModel(self):
        pass

    @abstractmethod
    def fitModel(self, X, y, checkpointPath):
        pass

    @abstractmethod
    def getModel(self):
        pass