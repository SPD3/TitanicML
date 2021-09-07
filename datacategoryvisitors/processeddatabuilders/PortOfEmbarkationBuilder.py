from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase

class PortOfEmbarkationBuilder (ProcessedDataBuilderBase):
    """Categorizes the port of embakation for each passenger."""

    def _buildProcessedData(self) -> None:
        """Creates assigns and appends a port mapping for each passenger to the 
        processed data."""
        for port in self._preprocessedData:
            self.__initializeCurrentPortMapping()
            self.__mapPort(port)
            self._processedData.append(self.__currentPortMapping)
    
    def __initializeCurrentPortMapping(self) -> None:
        """Creates the current port mapping with three bins."""
        self.__currentPortMapping = [0,0,0]
    
    def __mapPort(self, port: str) -> None:
        """Maps the port to a specific bin in currentPortMapping."""
        if(port == "S"):
            self.__currentPortMapping[0] = 1.0
        elif(port == "C"):
            self.__currentPortMapping[1] = 1.0
        else:
            self.__currentPortMapping[2] = 1.0