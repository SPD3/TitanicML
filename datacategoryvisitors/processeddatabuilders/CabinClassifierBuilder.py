from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase
import numpy as np

class CabinClassifierBuilder (ProcessedDataBuilderBase):
    """This processed data builder looks through the cabins for each passenger
    and maps them into different cabin bins."""

    def buildProcessedData(self) -> None:
        """Goes through all of the cabins for each passenger and categorizes 
        them into seperate bins"""
        for cabin in self.preprocessedData:
            self.initializeCabinMapping()
            self.mapCabin()
            self.processedData.append(self.currentCabinMapping)

    def initializeCabinMapping(self) -> None:
        """Initializes a passengers mapping with 9 bins."""
        self.currentCabinMapping = []
        for i in range(9):
            self.currentCabinMapping.append(0.0)

    def mapCabin(self, cabin) -> None:
        """Assigns a cabin value to a specific 
        bin based on letters inside the cabin value."""
        if(not type(cabin) == str):
            self.currentCabinMapping[0] = 1.0
        elif "A" in cabin:
            self.currentCabinMapping[1] = 1.0
        elif "B" in cabin:
            self.currentCabinMapping[2] = 1.0
        elif "C" in cabin:
            self.currentCabinMapping[3] = 1.0
        elif "D" in cabin:
            self.currentCabinMapping[4] = 1.0
        elif "E" in cabin:
            self.currentCabinMapping[5] = 1.0
        elif "F" in cabin:
            self.currentCabinMapping[6] = 1.0
        elif "T" in cabin:
            self.currentCabinMapping[7] = 1.0
        else:
            self.currentCabinMapping[8] = 1.0