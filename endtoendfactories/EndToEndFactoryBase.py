from abc import ABC, abstractmethod
from modelgenerators.ModelGeneratorBase import ModelGeneratorBase
from dataprocessors.DataProcessorBase import DataProcessorBase
import numpy as np

class EndToEndFactoryBase (ABC):
    """Base class from which all end-to-end factories derive from. End to end 
    factories build all of the necessary classes and objects to create a 
    sucessful ML pipeline. The objects needed to process the data initially all 
    the way to the model generator which creates the model based on the 
    processed data"""

    @abstractmethod
    def getPreProcessData(self, data:np.ndarray, dataIncludesLabels:bool) -> DataProcessorBase:
        pass

    @abstractmethod
    def getModelGenerator(self) -> ModelGeneratorBase:
        pass

    @abstractmethod
    def getName(self) -> str:
        pass