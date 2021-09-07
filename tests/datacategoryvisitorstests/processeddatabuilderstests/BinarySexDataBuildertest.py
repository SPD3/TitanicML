import unittest
from datacategoryvisitors.processeddatabuilders.BinarySexDataBuilder import BinarySexDataBuilder

class BinarySexDataBuilderTest (unittest.TestCase):
    """Tests the BinarySexDataBuilder class"""  
    def setUp(self) -> None:
        self.ageClassifierBuilder = BinarySexDataBuilder()

    def testBuildProcessedData(self) -> None:
        """Makes sure that buildProcessedData correctly categorizes males and 
        females in processedData"""
        preprocessedData = ["male","male","female","male","female"]
        self.ageClassifierBuilder._preprocessedData = preprocessedData
        self.ageClassifierBuilder.__buildProcessedData()
        solution = [[1.0],[1.0],[0.0],[1.0],[0.0]]
        self.assertEquals(solution, self.ageClassifierBuilder._processedData)
