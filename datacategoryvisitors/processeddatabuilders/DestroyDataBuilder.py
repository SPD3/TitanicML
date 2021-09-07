from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase

class DestroyDataBuilder (ProcessedDataBuilderBase):
    """Takes the data passed in as preprocessed data and gives back empty lists
    effectively destroying this data for each passenger"""

    def __buildProcessedData(self) -> None:
        """Adds an empty list to processed data for each passenger so that when 
        a client looks through this processed data they don't add anything to 
        each passenger for this data"""
        for item in self._preprocessedData:
            self._processedData.append([])