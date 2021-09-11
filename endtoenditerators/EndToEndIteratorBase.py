from abc import ABC, abstractmethod
from dataprocessors.DataProcessorWithVisitor import DataProcessorWithVisitor
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase
from dataprocessors.DataProcessorBase import DataProcessorBase
from typing import Tuple
import numpy as np
from modelgenerators.ModelGeneratorBase import ModelGeneratorBase

class EndToEndIteratorBase(ABC):
    """Base class for defining iteration through various end-to-end model 
    combinations. Subclasses will specify how the lists of data category 
    visitors, data processors, and model generators will be combined to form an 
    ML algorithm"""

    def __init__(self, dataCategoryVisitors:list[DataCategoryVisitorBase], 
        dataProcessors:list[DataProcessorWithVisitor], modelGenerators:list[ModelGeneratorBase]) -> None:
        super().__init__()
        self._dataCategoryVisitors = dataCategoryVisitors
        self._dataProcessors = dataProcessors
        self._modelGenerators = modelGenerators
        

    @abstractmethod
    def _first(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase]:
        """Gets the first X, Y, ModelGeneratorBase set and resets the iteration"""
        pass

    @abstractmethod
    def _next(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase]:
        """Increments the iterator and gets the next X, Y, ModelGeneratorBase 
        set"""
        pass

    @abstractmethod
    def _isDone(self) -> bool:
        """Tells when the iteration is finished"""
        pass

    @abstractmethod
    def _currentItem(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase]:
        """Tells when the iteration is finished"""
        pass

    def __iter__(self):
        """Python specific iteration method to support loops"""
        self._first()
        return self

    def __next__(self):
        """Python specific next method to support loops"""
        if(self._isDone()):
            raise StopIteration
        return self._next()