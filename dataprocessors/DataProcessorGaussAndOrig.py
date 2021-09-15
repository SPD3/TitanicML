from dataprocessors.DataProcessorWithVisitor import DataProcessorWithVisitor
import numpy as np
from dataprocessors.DataProcessorGaussianKernel import DataProcessorGaussianKernel

class DataProcessorGaussAndOrig (DataProcessorGaussianKernel):
    """Applies the gaussian kernel to each example but also tacks on the 
    original examples values"""

    def getProcessedData(self) -> tuple[np.ndarray, np.ndarray]:
        """Applies the gaussian filter with a call to super and then adds back 
        on the original data"""
        self._y, self._X = super().getProcessedData()
        self._X = self._X.tolist()
        self._addOrigXContentsOntoCurrentX()
        return np.array(self._y), np.array(self._X)

    def _addOrigXContentsOntoCurrentX(self) -> None:
        """Adds the original content for each example in X back onto X after the 
        gaussian filter."""
        for currentXExample, passengerIndex in zip(self._X, range(len(self._X))):
            for value, key in zip(self._categoryDictionary.values(), self._categoryDictionary.keys()):
                if(key == "Survived"):
                    continue
                currentXExample.extend(value[passengerIndex])

    def __str__(self) -> str:
        return "GaussAndOrigS:" + str(self._sigma)