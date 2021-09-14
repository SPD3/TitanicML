import math
import numpy as np
from datacategoryvisitors.ScaledDataCategoryVisitor import ScaledDataCategoryVisitor
from dataprocessors.DataProcessorGaussianKernel import DataProcessorGaussianKernel
import unittest

class DataProcessorGaussianKernelTest (unittest.TestCase):
    """Test class for the DataProcessorGaussianKernel class"""

    def setUp(self) -> None:
        data = [
            [1,0,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,1,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        self.dataProcessorGaussianKernel = DataProcessorGaussianKernel(data, True, ScaledDataCategoryVisitor())

    def testGetProcessedData(self) -> None:
        """Test the getProcessedData method"""
        y, X = self.dataProcessorGaussianKernel.getProcessedData()
        self.assertEquals(type(y), np.ndarray, msg="Y needs to be a numpy array")
        self.assertEquals(type(X), np.ndarray, msg="X needs to be a numpy array")
        self.assertEquals(len(y.shape), 1, msg="Y needs to be a 1d array")
        self.assertEquals(len(X.shape), 2, msg="X needs to be a 2d array")
        length = len(X[0])
        for example in X:
            self.assertEquals(len(example), length, msg="The examples in X need to be all the same length")

    def testApplyGaussianKernelToAllTrainingExamplesInX(self) -> None:
        """Makes sure that applyGaussianKernelToAllTrainingExamplesInX gets the 
        similary between ever example with every other example and modfifies X"""
        list1 = [1,2,3,4,5,6]
        list2 = [1,2,3,4,5,6]
        list3 = [8,9,10,11,12,13]
        self.dataProcessorGaussianKernel._X = [
            list1,
            list2,
            list3
        ]
        solution = [
            [
                self.dataProcessorGaussianKernel._getGaussianSimilarity(list1,list1),
                self.dataProcessorGaussianKernel._getGaussianSimilarity(list1,list2),
                self.dataProcessorGaussianKernel._getGaussianSimilarity(list1,list3),
            ],
            [
                self.dataProcessorGaussianKernel._getGaussianSimilarity(list2,list1),
                self.dataProcessorGaussianKernel._getGaussianSimilarity(list2,list2),
                self.dataProcessorGaussianKernel._getGaussianSimilarity(list2,list3),
            ],
            [
                self.dataProcessorGaussianKernel._getGaussianSimilarity(list3,list1),
                self.dataProcessorGaussianKernel._getGaussianSimilarity(list3,list2),
                self.dataProcessorGaussianKernel._getGaussianSimilarity(list3,list3),
            ],
        ]
        self.dataProcessorGaussianKernel._applyGaussianKernelToAllTrainingExamplesInX()
        self.assertEquals(self.dataProcessorGaussianKernel._X, solution)

    def testGetSimilarity(self) -> None:
        """Gets the similarity between two lists using a gaussian kernel"""
        list1 = [1,2,3,4,5,6]
        list2 = [1,2,3,4,5,6]
        list3 = [8,9,10,11,12,13]
        numerator = (8 - 1)**2 + (9 - 2)**2 + (10 - 3)**2 + (11 - 4)**2 + (12 - 5)**2 + (13 - 6)**2
        denominator = 2 * 1
        list1list3Similarity = math.e**(-numerator/denominator)
        self.assertEquals(self.dataProcessorGaussianKernel._getGaussianSimilarity(list1,list2), 1.0)
        self.assertEquals(self.dataProcessorGaussianKernel._getGaussianSimilarity(list1,list3), list1list3Similarity)

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
        self.assertEquals(self.dataProcessorGaussianKernel._getGaussianSimilarity(list1,list2), 1.0)
        self.assertEquals(self.dataProcessorGaussianKernel._getGaussianSimilarity(list1,list3), list1list3Similarity)

    def testString(self) -> None:
        """Tests the string representation of dataProcessorGaussianKernel"""
        self.assertEquals(str(self.dataProcessorGaussianKernel), "GausVisS:1.0")