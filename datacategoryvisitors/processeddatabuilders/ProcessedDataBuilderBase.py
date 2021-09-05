from abc import ABC, abstractmethod
from typing import List

class ProcessedDataBuilderBase (ABC):
    """Base class for processing data that initializes necessary variables for 
    the children classes"""

    def __init__(self) -> None:
        self.processedData = []

    @abstractmethod
    def buildProcessedData(self) -> None:
        pass

    def getProcessedData(self, preprocessedData:List) -> List:
        """
        Takes a list of data that has not been processed, builds processed data 
        based on this list and then returns this processed data
        
        Arguments
        ------------
        preprocessedData : a list of data to be processed so that a ML algorithm
            can interpret it
        
        returns: a list of the processed data in which each element is a list 
        that corresponds to a single passenger
        """
        self.preprocessedData = preprocessedData
        self.buildProcessedData()
        return self.processedData