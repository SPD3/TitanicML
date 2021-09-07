from typing import Tuple
from endtoenditerators.EndToEndIteratorBase import EndToEndIteratorBase
from modelgenerators.ModelGeneratorBase import ModelGeneratorBase
import numpy as np

class AllModelCombinationsIterator (EndToEndIteratorBase):
    
    def first(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase]:
        """Gets the first X, Y, ModelGeneratorBase set"""
        pass

    def next(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase]:
        """Increments the iterator and gets the next X, Y, ModelGeneratorBase 
        set"""
        pass

    def isDone(self) -> bool:
        """Tells when the iteration is finished"""
        pass

    def currentItem(self) -> Tuple[np.ndarray, np.ndarray, ModelGeneratorBase]:
        """Gets the current item"""
        pass