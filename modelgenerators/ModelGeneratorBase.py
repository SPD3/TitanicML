from abc import ABC, abstractmethod
import numpy as np
import tensorflow as tf

class ModelGeneratorBase (ABC):
    """Base class for creating models NN models to process the titanic data"""

    def __init__(self, inputShape:int, checkpoint_path:str) -> None:
        super().__init__()
        self.inputShape = inputShape
        self.checkpoint_path = checkpoint_path

    def getCheckpointPath(self) -> str:
        """Gets the path to this modelgenerator's save location"""
        return self.checkpoint_path

    @abstractmethod
    def createModel(self) -> None:
        pass

    @abstractmethod
    def fitModel(self, X:np.ndarray, y:np.ndarray, checkpointPath:str) -> None:
        pass

    @abstractmethod
    def getModel(self) -> tf.keras.Model:
        pass