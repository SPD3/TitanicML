import unittest

import numpy as np
from datacategoryvisitors.processeddatabuilders.AgeClassifierBuilder import AgeClassifierBuilder

class AgeClassifierBuilderTest (unittest.TestCase):
    """Tests the AgeClassifierBuilder class"""
    def setUp(self) -> None:
        self._ageClassifierBuilder = AgeClassifierBuilder()

    def testInitializeAgeMapping(self) -> None:
        """Makes sure that initializeAgeMapping() creates a list 11 bins long 
        and is all 0s"""
        self._ageClassifierBuilder._initializeAgeMapping()
        self.assertEquals(type(self._ageClassifierBuilder._currentAgeMapping), list)
        solution = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        self.assertEquals(solution, self._ageClassifierBuilder._currentAgeMapping)
    
    def testMapAge(self) -> None:
        """Makes sure that mapAge() maps various ages to the correct bin"""
        def testNewAgeValue(age:float, solution:list[float]):
            self._ageClassifierBuilder._initializeAgeMapping()
            self._ageClassifierBuilder._mapAge(age)
            self.assertEquals(solution, self._ageClassifierBuilder._currentAgeMapping)

        solution = [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        testNewAgeValue(5, solution)

        solution = [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        testNewAgeValue(np.nan, solution)

        solution = [0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0]
        testNewAgeValue(47, solution)

        solution = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0]
        testNewAgeValue(1030, solution)

    def testBuildProcessedData(self) -> None:
        """Makes sure that for every age passed in it is binned and appended to 
        processedData"""
        preprocessedData = [7.0, 56.0, np.nan, 512.0]
        self._ageClassifierBuilder._preprocessedData = preprocessedData
        self._ageClassifierBuilder._buildProcessedData()
        solution = [
            [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
            [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],
            [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
            [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0]
        ]
        self.assertEquals(solution, self._ageClassifierBuilder._processedData)
    
