from utilities.savehistories.SaveHistoriesBase import SaveHistoriesBase

class SaveAccAndValAccSeperateFiles (SaveHistoriesBase):

    def _createFilesWithLinesToSaveDict(self) -> None:
        """Creates the _filesWithLinesToSave dictionary. Every key in the 
        dictionary is name of the file to be saved, and every value associated 
        with a key is a list of lines to save to that file
        
        Creates two files: one for accuracy, and the other for validation 
        accuracy, and then creates all the lines to go into those files
        """
        self._filesWithLinesToSave = {
            "AccuracyComparison": [
                ["Epoch"]
            ],
            "ValAccuracyComparison": [
                ["Epoch"]
            ],
        }

        self._setUpEpochLines()

        
        for history, name in self.histories:
            self._addNameToFirstLine(name, self._filesWithLinesToSave["AccuracyComparison"])
            self._addNameToFirstLine(name, self._filesWithLinesToSave["ValAccuracyComparison"])

            self._addMetricToLines(history.history["accuracy"], self._filesWithLinesToSave["AccuracyComparison"][1:])
            self._addMetricToLines(history.history["val_accuracy"], self._filesWithLinesToSave["ValAccuracyComparison"][1:])

        
    def _addNameToFirstLine(self, name:str, list:list[list]) -> None:
        """Adds the specificed name to the first list item within the list 
        passed in"""
        list[0].append(name)

    def _setUpEpochLines(self):
        epochs = len(self.histories[0][0].history["val_accuracy"])
        for i in range(epochs):
            self._filesWithLinesToSave["AccuracyComparison"].append([i+1])
            self._filesWithLinesToSave["ValAccuracyComparison"].append([i+1])

    def _addMetricToLines(self, metric:list[float], lines:list[list[float]]):
        epoch = 1
        for line in lines:
            line.append(metric[epoch-1])
            epoch += 1