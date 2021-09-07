import unittest

import numpy as np
from datacategoryvisitors.processeddatabuilders.DataCategorizerBuilder import DataCategorizerBuilder

class DataCategorizerBuilderTest (unittest.TestCase):
    """Tests the DataCategorizerBuilder class"""
    def setUp(self) -> None:
        categories = [10,20,30,40,50]
        self.dataCategorizerBuilder = DataCategorizerBuilder(categories)

    def testGetIndexOfBin(self) -> None:
        """Makes sure that getIndexOfBin() returns the correct bin index given a
        particular value to be binned"""
        self.assertEquals(0, self.dataCategorizerBuilder.__getIndexOfBin(3))
        self.assertEquals(4, self.dataCategorizerBuilder.__getIndexOfBin(45))
        self.assertEquals(4, self.dataCategorizerBuilder.__getIndexOfBin(55))
        self.assertEquals(2, self.dataCategorizerBuilder.__getIndexOfBin(30))

    def testBuildProcessedData(self) -> None:
        """Makes sure that buildProcessedData appends the correctly filled bins 
        to processedData for the given values"""
        preprocessedData = [22, 42, 13, 40]
        self.dataCategorizerBuilder._preprocessedData = preprocessedData
        self.dataCategorizerBuilder._buildProcessedData()
        solution = [
            [0.0,0.0,1.0,0.0,0.0],
            [0.0,0.0,0.0,0.0,1.0],
            [0.0,1.0,0.0,0.0,0.0],
            [0.0,0.0,0.0,1.0,0.0]
        ]
        self.assertEquals(solution, self.dataCategorizerBuilder._processedData)