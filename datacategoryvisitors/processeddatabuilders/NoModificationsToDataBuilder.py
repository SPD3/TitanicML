from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase

class NoModificationsToDataBuilder (ProcessedDataBuilderBase):
    """Does not modify the contents of the data passed in, just reformats it to 
    be consistent with other builders"""

    def __buildProcessedData(self) -> None:
        """Reformats the data to be a list of lists and put this into processed 
        data because that is the format that clients expect"""
        for data in self._preprocessedData:
            self._processedData.append([data])