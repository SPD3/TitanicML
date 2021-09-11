from dataprocessors.DataProcessorWithVisitor import DataProcessorWithVisitor
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase
from typing import Tuple
from endtoenditerators.EndToEndIteratorBase import EndToEndIteratorBase
from modelgenerators.ModelGeneratorBase import ModelGeneratorBase
import numpy as np

class AllModelCombinationsIterator (EndToEndIteratorBase):
    """An iterator that takes in lists of data category visitors, data 
    processors with visitors, and model generators and then combines each item 
    of each list with each other to compare them against one another."""

    def __init__(self, dataCategoryVisitors:list[DataCategoryVisitorBase], 
        dataProcessorsWithVisitor:list[DataProcessorWithVisitor], modelGenerators:list[ModelGeneratorBase]) -> None:
        
        super().__init__(dataCategoryVisitors, dataProcessorsWithVisitor, modelGenerators)
        self._maxIndex = len(dataCategoryVisitors) * len(dataProcessorsWithVisitor) * len(modelGenerators)
        self._currentIndex = 0
    
    def _first(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase, str]:
        """Gets the first X, Y, ModelGeneratorBase set, and resets the 
        iteration"""
        self._currentIndex = 0
        return self._currentItem()

    def _next(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase, str]:
        """Increments the iterator and gets the next X, Y, ModelGeneratorBase 
        set"""
        self._currentIndex += 1
        return self._currentItem()

    def _isDone(self) -> bool:
        """Tells when the iteration is finished"""
        return (self._currentIndex >= self._maxIndex)

    def _currentItem(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase, str]:
        """Gets the current item"""
        dataCategoryVisitorsIndex, dataProcessorsIndex, modelGeneratorsIndex = self._getIndeciesOfCurrentItem()
        y, X = self._getYandX(dataCategoryVisitorsIndex, dataProcessorsIndex)
        name = self._getName()
        return (y, X, self._modelGenerators[modelGeneratorsIndex], name)

    def _getIndeciesOfCurrentItem(self) -> Tuple[int, int, int]:
        """Gets the idecies of the current visitor, dataprocessor and 
        ModelGeneratorBase"""
        localIndex = self._currentIndex
        modelGeneratorsIndex = localIndex % len(self._modelGenerators)

        localIndex = int(localIndex / len(self._modelGenerators))
        dataProcessorWithVisitorIndex = localIndex % len(self._dataProcessors)

        localIndex = int(localIndex / len(self._dataProcessors))
        dataCategoryVisitorsIndex = localIndex % len(self._dataCategoryVisitors)

        return (dataCategoryVisitorsIndex, dataProcessorWithVisitorIndex, modelGeneratorsIndex)

    def _getYandX(self, dataCategoryVisitorsIndex, dataProcessorsIndex):
        """Gets the data processor and visitor and processed the data"""
        dataProcessorWithVisitor = self._dataProcessors[dataProcessorsIndex]
        dataCategoryVisitor = self._dataCategoryVisitors[dataCategoryVisitorsIndex]
        dataProcessorWithVisitor.setDataCategoryVisitor(dataCategoryVisitor)
        return dataProcessorWithVisitor.getProcessedData()

    def _getName(self):
        """Creates and returns the name of the current indicies objects"""
        dataCategoryVisitorsIndex, dataProcessorsIndex, modelGeneratorsIndex = self._getIndeciesOfCurrentItem()
        name = str(self._dataCategoryVisitors[dataCategoryVisitorsIndex]) + "_" + \
            str(self._dataProcessors[dataProcessorsIndex]) + "_" + \
            str(self._modelGenerators[modelGeneratorsIndex])
        return name