from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase import ProcessedDataBuilderBase

class CompositeDataBuilder (ProcessedDataBuilderBase):

    def __init__(self, dataBuilders) -> None:
        super().__init__()
        self.dataBuilders = dataBuilders

    def buildProcessedData(self) -> None:
        self.processedData = self.preprocessedData
        for dataBuilder in self.dataBuilders:
            self.processedData = dataBuilder.getProcessedData(self.processedData)