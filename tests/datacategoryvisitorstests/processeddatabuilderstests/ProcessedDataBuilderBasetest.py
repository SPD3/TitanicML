import unittest

from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase import ProcessedDataBuilderBase

class ProcessedDataBuilderBaseTest (unittest.TestCase):
    
    def setUp(self) -> None:
        self._dummyProcessedDataBuilder = DummyProcessedDataBuilder()
    
    def testGetProcessedData(self) -> None:
        """Makes sure that when the dummy dummyProcessedDataBuilder is asked for 
        its processed data it processes its data before returning an answer"""
        solutionProcessedData = [1.0,2.0,3.0,4.0,5.0]
        preprocessedData = ["Hello" , "World"]
        processedData = self._dummyProcessedDataBuilder.getProcessedData(preprocessedData)
        self.assertEquals(solutionProcessedData, processedData)
        self.assertEquals(preprocessedData, self._dummyProcessedDataBuilder._preprocessedData)

class DummyProcessedDataBuilder (ProcessedDataBuilderBase):
    """Dummy ProcessedDataBuilder that just always builds the same processed 
    data"""
    def _buildProcessedData(self) -> None:
        self._processedData = [1.0,2.0,3.0,4.0,5.0]