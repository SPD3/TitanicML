import unittest

import numpy as np
from datacategoryvisitors.processeddatabuilders.PortOfEmbarkationBuilder import PortOfEmbarkationBuilder

class PortOfEmbarkationBuilderTest (unittest.TestCase):
    """Tests the PortOfEmbarkationBuilder class"""
    def setUp(self) -> None:
        self.portOfEmbarkationBuilder = PortOfEmbarkationBuilder()

    def testInitializeAgeMapping(self) -> None:
        """Makes sure that initializeCurrentPortMapping() creates a list 3 bins
        long and is all 0s"""
        self.portOfEmbarkationBuilder.initializeCurrentPortMapping()
        self.assertEquals(type(self.portOfEmbarkationBuilder.currentPortMapping), list)
        solution = [0.0,0.0,0.0]
        self.assertEquals(solution, self.portOfEmbarkationBuilder.currentPortMapping)

    def testMapPort(self) -> None:
        """Makes sure that mapPort() maps various ages to the correct bin"""
        def testNewPortValue(port, solution):
            self.portOfEmbarkationBuilder.initializeCurrentPortMapping()
            self.portOfEmbarkationBuilder.mapPort(port)
            self.assertEquals(solution, self.portOfEmbarkationBuilder.currentPortMapping)

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
        self.portOfEmbarkationBuilder.preprocessedData = preprocessedData
        self.portOfEmbarkationBuilder.buildProcessedData()
        solution = [
            [1.0,0.0,0.0],
            [0.0,0.0,1.0],
            [0.0,0.0,1.0],
            [0.0,1.0,0.0]
        ]
        self.assertEquals(solution, self.portOfEmbarkationBuilder.processedData)