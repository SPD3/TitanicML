from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase

class BinarySexDataBuilder (ProcessedDataBuilderBase):
    """This processed data builder assigns a value of 1.0 to male passengers 
    and 0.0 to female passengers"""

    def __buildProcessedData(self) -> None:
        """Looks at the sex for each passenger and assigns them a numerical 
        value accordingly"""
        for sex in self._preprocessedData:
            if sex == "male":
                self._processedData.append([1.0])
            else:
                self._processedData.append([0.0])