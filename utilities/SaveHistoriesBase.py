from abc import ABC, abstractmethod

class SaveHistoriesBase (ABC):

    def __init__(self, saveDst:str) -> None:
        self.histories = []
        self.saveDst = saveDst

    @abstractmethod
    def addHistory(self, history) -> None:
        pass

    @abstractmethod
    def saveAddedHistories(self) -> None:
        pass