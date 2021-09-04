from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase import ProcessedDataBuilderBase

class BinarySexDataBuilder (ProcessedDataBuilderBase):

    def buildProcessedData(self) -> None:
        for sex in self.preprocessedData:
            if sex == "male":
                self.processedData.append([1.0])
            else:
                self.processedData.append([0.0])