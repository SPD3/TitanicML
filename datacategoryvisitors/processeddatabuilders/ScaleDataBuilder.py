from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase import ProcessedDataBuilderBase

class ScaleDataBuilder (ProcessedDataBuilderBase):
    def __init__(self, scaleFactor) -> None:
        super().__init__()
        self.scaleFactor = scaleFactor

    def buildProcessedData(self) -> None:
        for data in self.preprocessedData:
            self.processedData.append([data * self.scaleFactor])