from abc import ABC, abstractmethod
from typing import List

class ProcessedDataBuilderBase (ABC):

    def __init__(self) -> None:
        self.processedData = []

    @abstractmethod
    def buildProcessedData(self) -> None:
        pass

    def getProcessedData(self, preprocessedData) -> List:
        self.preprocessedData = preprocessedData
        self.buildProcessedData()
        return self.processedData