from abc import ABC, abstractmethod

class ProcessedDataBuilderBase (ABC):
    """Base class for processing data that initializes necessary variables for 
    the children classes"""

    def __init__(self) -> None:
        self._processedData = []

    @abstractmethod
    def _buildProcessedData(self) -> None:
        pass

    def getProcessedData(self, preprocessedData:list) -> list:
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
        self._preprocessedData = preprocessedData
        self._buildProcessedData()
        return self._processedData