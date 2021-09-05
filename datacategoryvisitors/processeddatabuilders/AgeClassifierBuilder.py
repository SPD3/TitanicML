from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase
import numpy as np

class AgeClassifierBuilder (ProcessedDataBuilderBase):
    """This processed data builder looks through the ages for each passenger
    and maps them into different age bins."""

    def buildProcessedData(self) -> None:
        """Looks through all of the ages and maps them into bins"""
        for age in self.preprocessedData:
            self.initializeAgeMapping()
            self.mapAge(age)
            self.processedData.append(self.currentAgeMapping)

    def initializeAgeMapping(self) -> None:
        """Initializes a single age mapping list with 11 bins"""
        self.currentAgeMapping = []
        for i in range(11): 
            self.currentAgeMapping.append(0.0)

    def mapAge(self, age:float) -> None:
        """If the age is nan map it to the first bin, 
        otherwise map it to other bins based on how large it is"""
        if(np.isnan(age)):
            self.currentAgeMapping[0] = 1.0
        else:
            index = int(age / 8.0) + 1
            if(index > 10):
                index = 10
            self.currentAgeMapping[index] = 1.0