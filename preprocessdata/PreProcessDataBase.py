from abc import ABC, abstractmethod

class PreProcessDataBase (ABC):
    def __init__(self, data, dataIncludesLabels) -> None:
        super().__init__()
        self.data = data
        self.dataIncludesLabels = dataIncludesLabels
    
    @abstractmethod
    def getProcessedData(self):
        pass


