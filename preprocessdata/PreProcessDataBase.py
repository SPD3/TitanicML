from abc import ABC, abstractmethod

class PreProcessDataBase (ABC):
    def __init__(self, train_data, dataIncludesLabels) -> None:
        super().__init__()
        self.train_data = train_data
        self.dataIncludesLabels = dataIncludesLabels
    
    @abstractmethod
    def getProcessedData(self):
        pass


