from dataprocessors.DataProcessorGaussAndOrig import DataProcessorGaussAndOrig
from dataprocessors.DataProcessorGaussianKernel import DataProcessorGaussianKernel
from dataprocessors.DataProcessorWithVisitor import DataProcessorWithVisitor
import unittest
from datacategoryvisitors.ScaledDataCategoryVisitor import ScaledDataCategoryVisitor
import numpy as np

class DataPorcessorGaussAndOrigTest (unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            [1,0,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,1,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        self.dataProcessorGaussAndOrig = DataProcessorGaussAndOrig(self.data, True, ScaledDataCategoryVisitor())

    def testGetProcessedData(self) -> None:
        """Test the getProcessedData method"""
        y, X = self.dataProcessorGaussAndOrig.getProcessedData()
        self.assertEquals(type(y), np.ndarray, msg="Y needs to be a numpy array")
        self.assertEquals(type(X), np.ndarray, msg="X needs to be a numpy array")
        self.assertEquals(len(y.shape), 1, msg="Y needs to be a 1d array")
        self.assertEquals(len(X.shape), 2, msg="X needs to be a 2d array")
        length = len(X[0])
        for example in X:
            self.assertEquals(len(example), length, msg="The examples in X need to be all the same length")
        
        dataProcessorWithVisitor = DataProcessorWithVisitor(self.data, True, ScaledDataCategoryVisitor())
        dataProcessorGaussianKernel = DataProcessorGaussianKernel(self.data, True, ScaledDataCategoryVisitor())
        _, origX = dataProcessorWithVisitor.getProcessedData()
        _, gaussX = dataProcessorGaussianKernel.getProcessedData()
        gaussExampleLength = len(gaussX[0])

        X = X.tolist()
        origX = origX.tolist()
        gaussX = gaussX.tolist()

        for example, origExample, gaussExample in zip(X, origX, gaussX):
            self.assertEquals(example[:gaussExampleLength], gaussExample, msg="gauss example is not right")
            self.assertEquals(example[gaussExampleLength:], origExample, msg="orig example is not right")

    def testCombineOrigXAndGaussX(self) -> None:
        self.dataProcessorGaussAndOrig._X = [
            [1,2,3,4],
            [5,6,7,8],
        ]
        self.dataProcessorGaussAndOrig._categoryDictionary = {
            "PassengerId" : [[],[]],
            "Survived" : [[1,2,3,4],[5,55,5,5]],
            "Pclass" : [[],[]],
            "Name" : [[],[]],
            "Sex" : [[],[]],
            "Age" : [[],[]],
            "SibSp" : [[],[]],
            "Parch" : [[],[]],
            "Ticket" : [[],[]],
            "Fare" : [[],[]],
            "Cabin" : [[],[]],
            "Embarked" : [[2,3],[9,10]],
        }
        solution = [
            [1,2,3,4,2,3],
            [5,6,7,8,9,10],
        ]
        self.dataProcessorGaussAndOrig._addOrigXContentsOntoCurrentX()
        self.assertEquals(self.dataProcessorGaussAndOrig._X, solution)

    def testString(self) -> None:
        self.assertEquals(str(self.dataProcessorGaussAndOrig), "GaussAndOrigS:1.0")
        

    