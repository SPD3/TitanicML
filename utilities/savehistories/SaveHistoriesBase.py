from abc import ABC, abstractmethod
import csv

import tensorflow as tf

class SaveHistoriesBase (ABC):
    """Base class defining structure of classes that will take in model 
    histories and save them away in csv files to evaluate"""

    def __init__(self, name:str) -> None:
        self.histories = []
        self._filesWithLinesToSave = {}
        self.name = name

    def addHistory(self, history:tf.keras.callbacks.History, nameOfHistory:str) -> None:
        """Adds the history to a list of other histories"""
        self.histories.append((history, nameOfHistory))

    def saveAddedHistories(self) -> None:
        """Takes all of the histories that have been added up to this point and 
        saves them away into a file at saveDst"""
        self._filesWithLinesToSave = {}
        self._createFilesWithLinesToSaveDict()
        self._saveLinesToSave()

    @abstractmethod
    def _createFilesWithLinesToSaveDict(self) -> None:
        """Creates the _filesWithLinesToSave dictionary. Every key in the 
        dictionary is name of the file to be saved, and every value associated 
        with a key is a list of lines to save to that file"""
        pass

    def _saveLinesToSave(self) -> None:
        """Saves away all of the lines created within _filesWithLinesToSave"""
        for fileName in self._filesWithLinesToSave.keys():
            saveDst = "data/" + fileName + ".csv"
            linesToSave = self._filesWithLinesToSave[fileName]
            file = open(saveDst, "w")
            writer = csv.writer(file)
            for line in linesToSave:
                writer.writerow(line)
            file.close()
