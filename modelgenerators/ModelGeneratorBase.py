from abc import ABC, abstractmethod
import numpy as np
import tensorflow as tf

class ModelGeneratorBase (ABC):
    """Base class for creating models NN models to process the titanic data"""

    def __init__(self, inputShape:int, name:str) -> None:
        super().__init__()
        self.inputShape = inputShape
        self.name = name
        self.checkpoint_path = "savedmodels/" + self.name + "cp.ckpt1"

    def getCheckpointPath(self) -> str:
        """Gets the path to this modelgenerator's save location"""
        return self.checkpoint_path

    @abstractmethod
    def createModel(self) -> None:
        pass

    @abstractmethod
    def fitModel(self, X:np.ndarray, y:np.ndarray) -> tf.keras.callbacks.History:
        pass

    @abstractmethod
    def getModel(self) -> tf.keras.Model:
        pass