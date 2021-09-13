import math
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase
import numpy as np
from dataprocessors.DataProcessorWithVisitor import DataProcessorWithVisitor

class DataProcessorGaussianKernel (DataProcessorWithVisitor):
    def __init__(self, data: list[list], dataIncludesLabels: bool, dataCategoryVisitor: DataCategoryVisitorBase, sigma:float=1.0) -> None:
        super().__init__(data, dataIncludesLabels, dataCategoryVisitor=dataCategoryVisitor)
        self._sigma = sigma

    def getProcessedData(self) -> tuple[np.ndarray, np.ndarray]:
        self.y, self.X = super().getProcessedData()
        self._applyGaussianKernelToAllTrainingExamplesInX()
        return self.y, self.X

    def _applyGaussianKernelToAllTrainingExamplesInX(self) -> list[list[float]]:
        """Gets the similarity between every example in X with every other 
        example and then replaces the parameters of X with those values"""
        newX = []
        for example in self.X:
            newExampleEncoding = []
            for otherExample in self.X:
                newExampleEncoding.append(self._getSimilarity(example, otherExample))
            newX.append(newExampleEncoding)

        self.X = newX

    def _getSimilarity(self, list1:list[float], list2:list[float]) -> float:
        """Gets the similarity between two lists based on the formula:
        similarity = e^(-distanceBetweenLists^2/(2*(sigma^2)))
        """
        distance = 0
        for value1, value2 in zip(list1, list2):
            distance += (value2 - value1)**2
        return math.e**(-distance/(2 * self._sigma**2))