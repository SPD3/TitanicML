from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase

class PortOfEmbarkationBuilder (ProcessedDataBuilderBase):
    """Categorizes the port of embakation for each passenger."""

    def buildProcessedData(self) -> None:
        """Creates assigns and appends a port mapping for each passenger to the 
        processed data."""
        for port in self.preprocessedData:
            self.initializeCurrentPortMapping()
            self.mapPort(port)
            self.processedData.append(self.portMapping)
    
    def initializeCurrentPortMapping(self) -> None:
        """Creates the current port mapping with three bins."""
        self.currentPortMapping = [0,0,0]
    
    def mapPort(self, port: str) -> None:
        """Maps the port to a specific bin in currentPortMapping."""
        if(port == "S"):
            self.currentPortMapping[0] = 1.0
        elif(port == "C"):
            self.currentPortMapping[1] = 1.0
        else:
            self.currentPortMapping[2] = 1.0