from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase
import numpy as np

class ScaleDataBuilder (ProcessedDataBuilderBase):
    """Takes a list of data and returns that data scaled by a specified 
    scaleFactor"""
    def __init__(self, scaleFactor : float) -> None:
        super().__init__()
        self.__scaleFactor = scaleFactor

    def _buildProcessedData(self) -> None:
        """Scales the data for each passenger by the specified scaleFactor, 
        unless the data is nan, then it just gives the processed data a value 
        of zero"""
        for data in self._preprocessedData:
            if(np.isnan(data)):
                self._processedData.append([0.0])
            else:
                self._processedData.append([data * self.__scaleFactor])
