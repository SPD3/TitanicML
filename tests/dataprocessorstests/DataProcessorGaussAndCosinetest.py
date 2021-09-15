from datacategoryvisitors.ScaledDataCategoryVisitor import ScaledDataCategoryVisitor
import unittest

import numpy as np
from dataprocessors.DataProcessorGaussAndCosine import DataProcessorGaussAndCosine

class DataProcessorGaussAndCosineTest (unittest.TestCase):
    """Test code for the DataProcessorGaussAndCosine class"""
    def setUp(self) -> None:
        data = [
            [1,0,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,1,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        self.dataProcessorGaussAndCosine = DataProcessorGaussAndCosine(data, True, ScaledDataCategoryVisitor())

    def testGetCosineSimilarity(self):
        """Tests that the getCosineSimilarity method returns a value of 0 for 
        vectors that are orthogonal and a value of 1 for values that are in the 
        same direction"""
        list1 = [1,0,1,0]
        list2 = [0,1,0,1]
        list3 = [2,0,2,0]
        self.assertEquals(self.dataProcessorGaussAndCosine._getCosineSimilarity(list1, list2), 0)
        self.assertAlmostEquals(self.dataProcessorGaussAndCosine._getCosineSimilarity(list1, list3), 1.0, delta=0.01)

    def testString(self):
        self.assertEquals(str(self.dataProcessorGaussAndCosine), "GausCosS:1.0")