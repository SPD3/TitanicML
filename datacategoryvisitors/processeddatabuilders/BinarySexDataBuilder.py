from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase

class BinarySexDataBuilder (ProcessedDataBuilderBase):
    """This processed data builder assigns a value of 1.0 to male passengers 
    and 0.0 to female passengers"""

    def buildProcessedData(self) -> None:
        """Looks at the sex for each passenger and assigns them a numerical 
        value accordingly"""
        for sex in self.preprocessedData:
            if sex == "male":
                self.processedData.append([1.0])
            else:
                self.processedData.append([0.0])