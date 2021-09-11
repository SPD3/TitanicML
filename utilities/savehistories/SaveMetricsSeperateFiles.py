from utilities.savehistories.SaveHistoriesBase import SaveHistoriesBase

class SaveMetricsSeperateFiles (SaveHistoriesBase):

    def __init__(self, fileMetrics:list[tuple[str, list[str]]], name:str="") -> None:
        """The metrics list is a list in which every element corresponds to a 
        new file being created. Every element included the name of the file to 
        be created and a list which includes the metrics to be saved away in the
         file"""
        super().__init__(name)
        self.fileMetrics = fileMetrics

    def _createFilesWithLinesToSaveDict(self) -> None:
        """Creates the _filesWithLinesToSave dictionary. Every key in the 
        dictionary is name of the file to be saved, and every value associated 
        with a key is a list of lines to save to that file
        """
        self._filesWithLinesToSave = {}
        for fileName, metrics in self.fileMetrics:
            self._filesWithLinesToSave[fileName] = [["Epoch"]]

        self._setUpEpochLines()

        for history, name in self.histories:
            for fileName, metrics in self.fileMetrics:
                for metric in metrics:
                    self._addNameToFirstLine(name + metric, self._filesWithLinesToSave[fileName])
                    self._addMetricToLines(history.history[metric], self._filesWithLinesToSave[fileName][1:])

        
    def _addNameToFirstLine(self, name:str, list:list[list]) -> None:
        """Adds the specificed name to the first list item within the list 
        passed in"""
        list[0].append(name)

    def _setUpEpochLines(self):
        """Adds all of the epoch numbers for the histories to the categories
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