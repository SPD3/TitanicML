from abc import ABC, abstractmethod
import numpy as np

class PreProcessDataBase (ABC):
    """Base class that defines operations to convert data from csv file to 
    processed data that a ML algorith can use"""
    def __init__(self, data:list[list], dataIncludesLabels:bool) -> None:
        super().__init__()
        self._data = data
        self._dataIncludesLabels = dataIncludesLabels
        self._y = []
        self._X = []
    
    @abstractmethod
    def getProcessedData(self) -> tuple[np.ndarray, np.ndarray]:
        pass


