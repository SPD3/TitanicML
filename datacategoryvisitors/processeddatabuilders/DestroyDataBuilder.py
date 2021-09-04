from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase import ProcessedDataBuilderBase

class DestroyDataBuilder (ProcessedDataBuilderBase):

    def buildProcessedData(self) -> None:
        for item in self.preprocessedData:
            self.processedData.append([])