from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase
import numpy as np

class CabinClassifierBuilder (ProcessedDataBuilderBase):
    """This processed data builder looks through the cabins for each passenger
    and maps them into different cabin bins."""

    def _buildProcessedData(self) -> None:
        """Goes through all of the cabins for each passenger and categorizes 
        them into seperate bins"""
        for cabin in self._preprocessedData:
            self.__initializeCabinMapping()
            self.__mapCabin(cabin)
            self._processedData.append(self.__currentCabinMapping)

    def __initializeCabinMapping(self) -> None:
        """Initializes a passengers mapping with 9 bins."""
        self.__currentCabinMapping = []
        for i in range(9):
            self.__currentCabinMapping.append(0.0)

    def __mapCabin(self, cabin) -> None:
        """Assigns a cabin value to a specific 
        bin based on letters inside the cabin value."""
        if(not type(cabin) == str):
            self.__currentCabinMapping[0] = 1.0
        elif "A" in cabin:
            self.__currentCabinMapping[1] = 1.0
        elif "B" in cabin:
            self.__currentCabinMapping[2] = 1.0
        elif "C" in cabin:
            self.__currentCabinMapping[3] = 1.0
        elif "D" in cabin:
            self.__currentCabinMapping[4] = 1.0
        elif "E" in cabin:
            self.__currentCabinMapping[5] = 1.0
        elif "F" in cabin:
            self.__currentCabinMapping[6] = 1.0
        elif "T" in cabin:
            self.__currentCabinMapping[7] = 1.0
        else:
            self.__currentCabinMapping[8] = 1.0