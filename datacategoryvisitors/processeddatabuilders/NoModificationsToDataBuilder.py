from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase import ProcessedDataBuilderBase

class NoModificationsToDataBuilder (ProcessedDataBuilderBase):

    def buildProcessedData(self) -> None:
        for data in self.preprocessedData:
            self.processedData.append([data])