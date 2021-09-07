import unittest

import numpy as np
from datacategoryvisitors.processeddatabuilders.PortOfEmbarkationBuilder import PortOfEmbarkationBuilder

class PortOfEmbarkationBuilderTest (unittest.TestCase):
    """Tests the PortOfEmbarkationBuilder class"""
    def setUp(self) -> None:
        self._portOfEmbarkationBuilder = PortOfEmbarkationBuilder()

    def testInitializeAgeMapping(self) -> None:
        """Makes sure that initializeCurrentPortMapping() creates a list 3 bins
        long and is all 0s"""
        self._portOfEmbarkationBuilder._initializeCurrentPortMapping()
        self.assertEquals(type(self._portOfEmbarkationBuilder._currentPortMapping), list)
        solution = [0.0,0.0,0.0]
        self.assertEquals(solution, self._portOfEmbarkationBuilder._currentPortMapping)

    def testMapPort(self) -> None:
        """Makes sure that mapPort() maps various ages to the correct bin"""
        def testNewPortValue(port:str, solution:list[float]):
            self._portOfEmbarkationBuilder._initializeCurrentPortMapping()
            self._portOfEmbarkationBuilder._mapPort(port)
            self.assertEquals(solution, self._portOfEmbarkationBuilder._currentPortMapping)

        solution = [0.0,1.0,0.0]
        testNewPortValue("C", solution)

        solution = [1.0,0.0,0.0]
        testNewPortValue("S", solution)

        solution = [0.0,0.0,1.0]
        testNewPortValue("Q", solution)

    def testBuildProcessedData(self) -> None:
        """Makes sure that for every port passed in it is binned and appended to 
        processedData"""
        preprocessedData = ["S", "Q", "Q", "C"]
        self._portOfEmbarkationBuilder._preprocessedData = preprocessedData
        self._portOfEmbarkationBuilder._buildProcessedData()
        solution = [
            [1.0,0.0,0.0],
            [0.0,0.0,1.0],
            [0.0,0.0,1.0],
            [0.0,1.0,0.0]
        ]
        self.assertEquals(solution, self._portOfEmbarkationBuilder._processedData)