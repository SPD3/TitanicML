import math
from datacategoryvisitors.ScaledDataCategoryVisitor import ScaledDataCategoryVisitor
from dataprocessors.DataProcessorGaussianKernel import DataProcessorGaussianKernel
import unittest

class DataProcessorGaussianKernelTest (unittest.TestCase):
    """Test class for the DataProcessorGaussianKernel class"""

    def setUp(self) -> None:
        data = [[]]
        self.dataProcessorGaussianKernel = DataProcessorGaussianKernel(data, True, ScaledDataCategoryVisitor())

    def testApplyGaussianKernelToAllTrainingExamplesInX(self) -> None:
        """Makes sure that applyGaussianKernelToAllTrainingExamplesInX gets the 
        similary between ever example with every other example and modfifies X"""
        list1 = [1,2,3,4,5,6]
        list2 = [1,2,3,4,5,6]
        list3 = [8,9,10,11,12,13]
        self.dataProcessorGaussianKernel.X = [
            list1,
            list2,
            list3
        ]
        solution = [
            [
                self.dataProcessorGaussianKernel._getSimilarity(list1,list1),
                self.dataProcessorGaussianKernel._getSimilarity(list1,list2),
                self.dataProcessorGaussianKernel._getSimilarity(list1,list3),
            ],
            [
                self.dataProcessorGaussianKernel._getSimilarity(list2,list1),
                self.dataProcessorGaussianKernel._getSimilarity(list2,list2),
                self.dataProcessorGaussianKernel._getSimilarity(list2,list3),
            ],
            [
                self.dataProcessorGaussianKernel._getSimilarity(list3,list1),
                self.dataProcessorGaussianKernel._getSimilarity(list3,list2),
                self.dataProcessorGaussianKernel._getSimilarity(list3,list3),
            ],
        ]
        self.dataProcessorGaussianKernel._applyGaussianKernelToAllTrainingExamplesInX()
        self.assertEquals(self.dataProcessorGaussianKernel.X, solution)

    def testGetSimilarity(self) -> None:
        """Gets the similarity between two lists using a gaussian kernel"""
        list1 = [1,2,3,4,5,6]
        list2 = [1,2,3,4,5,6]
        list3 = [8,9,10,11,12,13]
        numerator = (8 - 1)**2 + (9 - 2)**2 + (10 - 3)**2 + (11 - 4)**2 + (12 - 5)**2 + (13 - 6)**2
        denominator = 2 * 1
        list1list3Similarity = math.e**(-numerator/denominator)
        self.assertEquals(self.dataProcessorGaussianKernel._getSimilarity(list1,list2), 1.0)
        self.assertEquals(self.dataProcessorGaussianKernel._getSimilarity(list1,list3), list1list3Similarity)

    def testGetSimilarityNewSigma(self) -> None:
        """Gets the similarity between two lists using a gaussian kernel but 
        with a sigma other than 1"""
        self.dataProcessorGaussianKernel._sigma = 2.0
        list1 = [1,2,3,4,5,6]
        list2 = [1,2,3,4,5,6]
        list3 = [8,9,10,11,12,13]
        numerator = (8 - 1)**2 + (9 - 2)**2 + (10 - 3)**2 + (11 - 4)**2 + (12 - 5)**2 + (13 - 6)**2
        denominator = 2 * 2**2
        list1list3Similarity = math.e**(-numerator/denominator)
        self.assertEquals(self.dataProcessorGaussianKernel._getSimilarity(list1,list2), 1.0)
        self.assertEquals(self.dataProcessorGaussianKernel._getSimilarity(list1,list3), list1list3Similarity)