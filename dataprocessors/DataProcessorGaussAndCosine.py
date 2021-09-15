import numpy as np
from dataprocessors.DataProcessorGaussianKernel import DataProcessorGaussianKernel

class DataProcessorGaussAndCosine (DataProcessorGaussianKernel):

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
                newExampleEncoding.append(self._getCosineSimilarity(example, otherExample))
            newX.append(newExampleEncoding)

        self._X = newX
        
    def _getCosineSimilarity(self, list1:list[float], list2:list[float]) -> float:
        """Gets the cosine similarity between two list of values."""
        dot = 0
        list1Mag = 0
        list2Mag = 0
        for value1, value2 in zip(list1, list2):
            dot += value1 * value2
            list1Mag += value1**2
            list2Mag += value2**2

        list1Mag = list1Mag**0.5
        list2Mag = list2Mag**0.5
        return dot / (list1Mag * list2Mag)

    def __str__(self) -> str:
        return "GausCosS:" + str(self._sigma)
