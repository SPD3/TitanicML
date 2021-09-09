from abc import ABC, abstractmethod
from preprocessdata.DataPreProcessorWithVisitor import DataPreProcessorWithVisitor
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase
from preprocessdata.PreProcessDataBase import PreProcessDataBase
from typing import Tuple
import numpy as np
from modelgenerators.ModelGeneratorBase import ModelGeneratorBase

class EndToEndIteratorBase(ABC):

    def __init__(self, dataCategoryVisitors:list[DataCategoryVisitorBase], 
        dataProcessors:list[DataPreProcessorWithVisitor], modelGenerators:list[ModelGeneratorBase]) -> None:
        super().__init__()
        self._dataCategoryVisitors = dataCategoryVisitors
        self._dataProcessors = dataProcessors
        self._modelGenerators = modelGenerators
        

    @abstractmethod
    def first(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase]:
        """Gets the first X, Y, ModelGeneratorBase set and resets the iteration"""
        pass

    @abstractmethod
    def next(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase]:
        """Increments the iterator and gets the next X, Y, ModelGeneratorBase 
        set"""
        pass

    @abstractmethod
    def isDone(self) -> bool:
        """Tells when the iteration is finished"""
        pass

    @abstractmethod
    def currentItem(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase]:
        """Tells when the iteration is finished"""
        pass