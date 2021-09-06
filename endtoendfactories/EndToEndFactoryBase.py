from abc import ABC, abstractmethod
from modelgenerators.ModelGeneratorBase import ModelGeneratorBase
from preprocessdata.PreProcessDataBase import PreProcessDataBase
import numpy as np

class EndToEndFactoryBase (ABC):

    @abstractmethod
    def getPreProcessData(self, data:np.ndarray, dataIncludesLabels:bool) -> PreProcessDataBase:
        pass

    @abstractmethod
    def getModelGenerator(self, inputShape:int) -> ModelGeneratorBase:
        pass