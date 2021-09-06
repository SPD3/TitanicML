from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase

class DataCategorizerBuilder (ProcessedDataBuilderBase):
    """Categorizes preprocessed data into seperate bins specified by the user"""

    def __init__(self, categories:list[float]) -> None:
        """
        Parameters
        ---------------
        categories : an ordered list of the highest value for each category
        """
        super().__init__()
        self.categories = categories

    def buildProcessedData(self) -> None:
        """Goes through all the values for each passenger in preprocessed data 
        and assigns them to a category """
        for value in self.preprocessedData:
            currentData = [0] * len(self.categories)
            i = self.getIndexOfBin(value)
            currentData[i] = 1.0
            self.processedData.append(currentData)

    def getIndexOfBin(self, value: float) -> int:
        """Looks for the first category in which the value falls below 
        the categories cut off and returns this index"""
        for i in range(len(self.categories)):
            if value <= self.categories[i]:
                break
        return i