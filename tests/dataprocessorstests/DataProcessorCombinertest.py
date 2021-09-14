import math
import numpy as np
from dataprocessors.DataProcessorCombiner import DataProcessorCombiner
import unittest
from datacategoryvisitors.ScaledDataCategoryVisitor import ScaledDataCategoryVisitor

class DataProcessorCombinerTest (unittest.TestCase):
    """Test code for the DataProcessorCombiner class"""
    def setUp(self) -> None:
        data = [
            [1,0,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,1,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        self.dataProcessorCombiner = DataProcessorCombiner(data, True, ScaledDataCategoryVisitor())

    def testAddDataCombinationsToX(self) -> None:
        """Tests the addDataCombinationsToX method"""
        self.dataProcessorCombiner._X = [
            [1,0,1],
            [0.5,0.3,0.4]
        ]
        self.dataProcessorCombiner._addDataCombinationsToX()
        solution = [
            [1,0,1,0,1,0],
            [0.5,0.3,0.4,math.sqrt(0.5*0.3), math.sqrt(0.5*0.4), math.sqrt(0.3*0.4)]
        ]
        self.assertEquals(self.dataProcessorCombiner._X , solution)

    def testGetProcessedData(self) -> None:
        """Test the getProcessedData method"""
        y, X = self.dataProcessorCombiner.getProcessedData()
        self.assertEquals(type(y), np.ndarray, msg="Y needs to be a numpy array")
        self.assertEquals(type(X), np.ndarray, msg="X needs to be a numpy array")
        self.assertEquals(len(y.shape), 1, msg="Y needs to be a 1d array")
        self.assertEquals(len(X.shape), 2, msg="X needs to be a 2d array")
        length = len(X[0])
        for example in X:
            self.assertEquals(len(example), length, msg="The examples in X need to be all the same length")

    def testString(self) -> None:
        """Tests the string representation of DataProcessorCombiner"""
        self.assertEquals(str(self.dataProcessorCombiner), "DataProcCombine")