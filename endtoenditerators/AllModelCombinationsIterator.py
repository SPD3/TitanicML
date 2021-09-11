from preprocessdata.DataPreProcessorWithVisitor import DataPreProcessorWithVisitor
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase
from typing import Tuple
from endtoenditerators.EndToEndIteratorBase import EndToEndIteratorBase
from modelgenerators.ModelGeneratorBase import ModelGeneratorBase
from preprocessdata.PreProcessDataBase import PreProcessDataBase
import numpy as np

class AllModelCombinationsIterator (EndToEndIteratorBase):
    def __init__(self, dataCategoryVisitors:list[DataCategoryVisitorBase], 
        dataProcessorsWithVisitor:list[DataPreProcessorWithVisitor], modelGenerators:list[ModelGeneratorBase]) -> None:
        
        super().__init__(dataCategoryVisitors, dataProcessorsWithVisitor, modelGenerators)
        self._maxIndex = len(dataCategoryVisitors) * len(dataProcessorsWithVisitor) * len(modelGenerators)
        self._currentIndex = 0
    
    def _first(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase]:
        """Gets the first X, Y, ModelGeneratorBase set, and resets the 
        iteration"""
        self._currentIndex = 0
        return self._currentItem()

    def _next(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase]:
        """Increments the iterator and gets the next X, Y, ModelGeneratorBase 
        set"""
        self._currentIndex += 1
        return self._currentItem()

    def _isDone(self) -> bool:
        """Tells when the iteration is finished"""
        return (self._currentIndex >= self._maxIndex)

    def _currentItem(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase]:
        """Gets the current item"""
        dataCategoryVisitorsIndex, dataProcessorsIndex, modelGeneratorsIndex = self._getIndeciesOfCurrentItem()
        y, X = self._getYandX(dataCategoryVisitorsIndex, dataProcessorsIndex)
        return (y, X, self._modelGenerators[modelGeneratorsIndex])

    def _getIndeciesOfCurrentItem(self) -> Tuple[int, int, int]:
        localIndex = self._currentIndex
        modelGeneratorsIndex = localIndex % len(self._modelGenerators)

        localIndex = int(localIndex / len(self._modelGenerators))
        dataProcessorWithVisitorIndex = localIndex % len(self._dataProcessors)

        localIndex = int(localIndex / len(self._dataProcessors))
        dataCategoryVisitorsIndex = localIndex % len(self._dataCategoryVisitors)

        return (dataCategoryVisitorsIndex, dataProcessorWithVisitorIndex, modelGeneratorsIndex)

    def _getYandX(self, dataCategoryVisitorsIndex, dataProcessorsIndex):
        dataProcessorWithVisitor = self._dataProcessors[dataProcessorsIndex]
        dataCategoryVisitor = self._dataCategoryVisitors[dataCategoryVisitorsIndex]
        dataProcessorWithVisitor.setDataCategoryVisitor(dataCategoryVisitor)
        return dataProcessorWithVisitor.getProcessedData()