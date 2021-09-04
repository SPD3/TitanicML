from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase import ProcessedDataBuilderBase
import numpy as np

class ReplaceNanWithZeroBuilder (ProcessedDataBuilderBase):

    def buildProcessedData(self) -> None:
        for data in self.preprocessedData:
            if(np.isnan(data)):
                self.processedData.append(0.0) 
                # not putting 0.0 in its own list because ReplaceNanWithZeroBuilder 
                # is supposed to be used in conjunction with other builders which will 
                # do that work for you
            else:
                self.processedData.append(data)