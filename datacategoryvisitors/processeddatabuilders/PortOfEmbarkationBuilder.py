from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase

class PortOfEmbarkationBuilder (ProcessedDataBuilderBase):
    """Categorizes the port of embakation for each passenger."""

    def __buildProcessedData(self) -> None:
        """Creates assigns and appends a port mapping for each passenger to the 
        processed data."""
        for port in self._preprocessedData:
            self.__initializeCurrentPortMapping()
            self.__mapPort(port)
            self._processedData.append(self._currentPortMapping)
    
    def __initializeCurrentPortMapping(self) -> None:
        """Creates the current port mapping with three bins."""
        self._currentPortMapping = [0,0,0]
    
    def __mapPort(self, port: str) -> None:
        """Maps the port to a specific bin in currentPortMapping."""
        if(port == "S"):
            self._currentPortMapping[0] = 1.0
        elif(port == "C"):
            self._currentPortMapping[1] = 1.0
        else:
            self._currentPortMapping[2] = 1.0