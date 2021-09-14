import math
import numpy as np
from dataprocessors.DataProcessorWithVisitor import DataProcessorWithVisitor

class DataProcessorCombiner (DataProcessorWithVisitor):

    def getProcessedData(self) -> tuple[np.ndarray, np.ndarray]:
        self._y, self._X = super().getProcessedData()
        self._y = self._y.tolist()
        self._X = self._X.tolist()
        self._addDataCombinationsToX()
        return np.array(self._y), np.array(self._X)

    def _addDataCombinationsToX(self) -> None:
        """takes every category of data for each example and combines it with 
        the other categories, then appends that combination onto that example's 
        list in X"""
        for example, indexInX in zip(self._X, range(len(self._X))):
            betterExample = example.copy()
            for value, index in zip(example, range(len(example))):
                for otherValue in example[index+1:]:   
                    betterExample.append(math.sqrt(value * otherValue))
            self._X[indexInX] = betterExample

    def __str__(self) -> str:
        return "DataProcCombine"
