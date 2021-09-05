from abc import ABC, abstractmethod
import numpy as np
import tensorflow as tf

class ModelGeneratorBase (ABC):
    """Base class for creating models NN models to process the titanic data"""

    @abstractmethod
    def createModel(self) -> None:
        pass

    @abstractmethod
    def fitModel(self, X:np.ndarray, y:np.ndarray, checkpointPath:str) -> None:
        pass

    @abstractmethod
    def getModel(self) -> tf.keras.Model:
        pass