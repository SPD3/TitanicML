from abc import ABC, abstractmethod

class FactoryBase (ABC):

    @abstractmethod
    def getDataPreProcessor(self, data, dataIncludesLabels):
        pass

    @abstractmethod
    def getModel(self, inputShape):
        pass

    @abstractmethod
    def getDataCategoryVisitor(self):
        pass