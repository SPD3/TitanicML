import unittest

import numpy as np
from datacategoryvisitors.processeddatabuilders.DestroyDataBuilder import DestroyDataBuilder

class DestroyDataBuilderTest (unittest.TestCase):
    """Tests the DestroyDataBuilder class"""
    def setUp(self) -> None:
        self.destroyDataBuilder = DestroyDataBuilder()
    
    def testBuildProcessedData(self) -> None:
        """Makes sure that no matter the data passed in, destroyDataBuilder will
        give back a list of empty lists"""
        preprocessedData = [1.0, 32, "Hello World", [[[]]]]
        self.destroyDataBuilder._preprocessedData = preprocessedData
        self.destroyDataBuilder._buildProcessedData()
        solution = [[],[],[],[]]
        self.assertEquals(solution, self.destroyDataBuilder._processedData)