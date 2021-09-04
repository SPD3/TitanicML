from abc import ABC, abstractmethod

class ModelBase (ABC):

    @abstractmethod
    def createModel(inputShape):
        pass