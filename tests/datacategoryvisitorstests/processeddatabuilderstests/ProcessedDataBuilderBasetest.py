import unittest

from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase import ProcessedDataBuilderBase

class DummyProcessedDataBuilder (ProcessedDataBuilderBase):
    """Dummy ProcessedDataBuilder that just always builds the same processed 
    data"""
    def buildProcessedData(self) -> None:
        self.processedData = [1.0,2.0,3.0,4.0,5.0]

class ProcessedDataBuilderBaseTest (unittest.TestCase):
    
    def setUp(self) -> None:
        self.dummyProcessedDataBuilder = DummyProcessedDataBuilder()
    
    def testGetProcessedData(self) -> None:
        """Makes sure that when the dummy dummyProcessedDataBuilder is asked for 
        its processed data it processes its data before returning an answer"""
        solutionProcessedData = [1.0,2.0,3.0,4.0,5.0]
        preprocessedData = ["Hello" , "World"]
        processedData = self.dummyProcessedDataBuilder.getProcessedData(preprocessedData)
        self.assertEquals(solutionProcessedData, processedData)
        self.assertEquals(preprocessedData, self.dummyProcessedDataBuilder.preprocessedData)