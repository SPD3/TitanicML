import unittest

import numpy as np
from datacategoryvisitors.processeddatabuilders.ScaleDataBuilder import ScaleDataBuilder

class ScaleDataBuilderTest (unittest.TestCase):
    """Tests the ScaleDataBuilder class"""
    def setUp(self) -> None:
        """Sets up then scaleDataBuilder with a scale factor of 0.5"""
        self.scaleDataBuilder = ScaleDataBuilder(0.5)

    def testBuildProcessedData(self) -> None:
        """Makes sure that the preprocessed data is scaled by 0.5 and then is 
        appended onto the end of processedData"""

        preprocessedData = [1.0, 82, 53, 1024]
        self.scaleDataBuilder._preprocessedData = preprocessedData
        self.scaleDataBuilder.__buildProcessedData()
        solution = [[0.5], [41], [26.5], [512]]
        self.assertEquals(solution, self.scaleDataBuilder._processedData)