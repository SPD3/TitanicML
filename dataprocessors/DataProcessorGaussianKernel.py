from datacategoryvisitors.CategorizedDataVisitor import CategorizedDataVisitor
import math
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase
import numpy as np
from dataprocessors.DataProcessorWithVisitor import DataProcessorWithVisitor

class DataProcessorGaussianKernel (DataProcessorWithVisitor):
    """Applies a gaussian kernel to compare every example with all other 
    examples and uses these values to make up the features of each example"""

    def __init__(self, data: list[list], dataIncludesLabels: bool, dataCategoryVisitor:DataCategoryVisitorBase=CategorizedDataVisitor, sigma:float=1.0, dataToCompareTo:list[list[float]]=None) -> None:
        super().__init__(data, dataIncludesLabels, dataCategoryVisitor=dataCategoryVisitor)
        self._sigma = sigma
        self._dataToCompareTo = dataToCompareTo

    def getProcessedData(self) -> tuple[np.ndarray, np.ndarray]:
        """Gets the processed data from visitors with a call to super's 
        getprocessedData and then applies the gaussian kernel to these examples"""
        self._y, self._X = super().getProcessedData()
        self._applyGaussianKernelToAllTrainingExamplesInX()
        return np.array(self._y), np.array(self._X)

    def _applyGaussianKernelToAllTrainingExamplesInX(self) -> list[list[float]]:
        """Gets the similarity between every example in X with every other 
        example and then replaces the parameters of X with those values"""
        newX = []
        try:
            if self._dataToCompareTo == None:
                self._dataToCompareTo = self._X
        except ValueError:
            #this means that _dataToCompareTo has something in it and will throw
            #an excpetion when being compared to None
            pass

        for example in self._X:
            newExampleEncoding = []
            for otherExample in self._dataToCompareTo:
                newExampleEncoding.append(self._getGaussianSimilarity(example, otherExample))
            newX.append(newExampleEncoding)

        self._X = newX

    def _getGaussianSimilarity(self, list1:list[float], list2:list[float]) -> float:
        """Gets the similarity between two lists based on the formula:
        similarity = e^(-distanceBetweenLists^2/(2*(sigma^2)))
        """
        distance = 0
        for value1, value2 in zip(list1, list2):
            distance += (value2 - value1)**2
        return math.e**(-distance/(2 * self._sigma**2))

    def __str__(self) -> str:
        return "GausVisS:" + str(self._sigma)