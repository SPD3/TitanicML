import unittest

from datacategoryvisitors.processeddatabuilders.NoModificationsToDataBuilder import NoModificationsToDataBuilder

class NoModificationsToDataBuilderTest (unittest.TestCase):
    """Tests the NoModificationsToDataBuilder class"""
    def setUp(self) -> None:
        self.noModificationsToDataBuilder = NoModificationsToDataBuilder()

    def testBuildProcessedData(self) -> None:
        """Makes sure that the content of preprecessedData stays the same and 
        that it's format is only changed in processedData to be a list of lists"""
        preprocessedData = [1.0, "Goodbye", 1234, [1,2,3,4]]
        self.noModificationsToDataBuilder._preprocessedData = preprocessedData
        self.noModificationsToDataBuilder._buildProcessedData()
        solution = [
            [1.0],
            ["Goodbye"],
            [1234],
            [[1,2,3,4]]
        ]
        self.assertEquals(solution, self.noModificationsToDataBuilder._processedData)