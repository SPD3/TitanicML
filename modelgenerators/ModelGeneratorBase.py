from abc import ABC, abstractmethod
import numpy as np
import tensorflow as tf

class ModelGeneratorBase (ABC):
    """Base class for creating models NN models to process the titanic data"""

    def __init__(self, name:str) -> None:
        super().__init__()
        self._name = name
        self._checkpoint_path = "savedmodels/" + self._name + "cp.ckpt1"

    def getCheckpointPath(self) -> str:
        """Gets the path to this modelgenerator's save location"""
        return self._checkpoint_path

    @abstractmethod
    def createModel(self, inputShape:int) -> tf.keras.Model:
        """Creates and returns a new model"""
        pass

    @abstractmethod
    def fitModel(self, X:np.ndarray, y:np.ndarray) -> tf.keras.callbacks.History:
        """Fits a model to the training set and labels"""
        pass

    @abstractmethod
    def getModel(self) -> tf.keras.Model:
        """Gets the current model"""
        pass