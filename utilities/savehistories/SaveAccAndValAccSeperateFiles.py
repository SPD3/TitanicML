from utilities.savehistories.SaveHistoriesBase import SaveHistoriesBase

class SaveAccAndValAccSeperateFiles (SaveHistoriesBase):
    """A class to save the accuracy and validation accuracy of various models """

    def __init__(self, name:str="") -> None:
        super().__init__(name)

    def _createFilesWithLinesToSaveDict(self) -> None:
        """Creates the _filesWithLinesToSave dictionary. Every key in the 
        dictionary is name of the file to be saved, and every value associated 
        with a key is a list of lines to save to that file
        
        Creates two files: one for accuracy, and the other for validation 
        accuracy, and then creates all the lines to go into those files
        """
        self._filesWithLinesToSave = {
            self.name + "AccuracyComparison": [
                ["Epoch"]
            ],
            self.name + "ValAccuracyComparison": [
                ["Epoch"]
            ],
        }

        self._setUpEpochLines()

        
        for history, name in self.histories:
            for fileName in self._filesWithLinesToSave.keys():
                self._addNameToFirstLine(name, self._filesWithLinesToSave[fileName])

            metricsCorrespondingToFileNames = ["accuracy", "val_accuracy"]
            for metricName, fileName in zip(metricsCorrespondingToFileNames, self._filesWithLinesToSave.keys()):
                self._addMetricToLines(history.history[metricName], self._filesWithLinesToSave[fileName][1:])

        
    def _addNameToFirstLine(self, name:str, list:list[list]) -> None:
        """Adds the specificed name to the first list item within the list 
        passed in"""
        list[0].append(name)

    def _setUpEpochLines(self):
        """Adds all of the epoch numbers for the histories to the two categories
         to be logged"""
        epochs = len(self.histories[0][0].history["val_accuracy"])
        for i in range(epochs):
            for fileName in self._filesWithLinesToSave.keys():
                self._filesWithLinesToSave[fileName].append([i+1])

    def _addMetricToLines(self, metric:list[float], lines:list[list[float]]):
        """Takes a list of numbers that make up a metric and add them to the 
        epochs the correspond to within the lines argument"""
        epoch = 1
        for line in lines:
            line.append(metric[epoch-1])
            epoch += 1