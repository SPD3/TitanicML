from modelgenerators.ModelGeneratorBase import ModelGeneratorBase
import tensorflow as tf
import numpy as np

class RectangularDenseModelGenerator (ModelGeneratorBase):
    """Creates a NN with the same layersize for all layers specified"""

    def __init__(self, name:str, layerSize:int=512, layers:int=10, epochs:int=40, learningRate:float=5.0e-5) -> None:
        """
        Arguments:
        -----------
        inputShape: the size of the input tensor
        layersize: the desired number of nodes for each layer
        layers: the desired number of layers between the input and sigmoid output layer
        epochs: the number of epochs to train for
        learningRate: The learning rate applied per epoch
        """
        super().__init__(name)
        self._layerSize = layerSize
        self._layers = layers
        self._epochs = epochs
        self._validation_split = 0.1
        self._model = None
        self._learningRate = learningRate
        self._inputShape = None

    def createModel(self, inputShape:int) -> tf.keras.Model:
        """Sets up connections between layers, creates and compiles a model"""
        self._inputShape = inputShape
        self._createInputsLinkedToOutputs()
        self._model = tf.keras.Model(inputs=self._inputs, outputs=self._outputs)
        self._compileModel()
        return self._model

    def _createInputsLinkedToOutputs(self) -> None:
        """Sets up the layers between the input and output layers"""
        self._inputs = tf.keras.layers.Input(shape=(self._inputShape))
        x = tf.keras.layers.Dense(self._layerSize, activation="relu")(self._inputs)
        for i in range(self._layers - 1):
            x = tf.keras.layers.Dense(self._layerSize, activation="relu")(x)
        self._outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)
    
    def _compileModel(self) -> None:
        """Compiles the model with the adam optimizer."""
        self._model.compile(
            optimizer=tf.keras.optimizers.Adam(self._learningRate),
            loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
            metrics=["accuracy"]
        )
    
    def getModel(self) -> tf.keras.Model:
        """Gets the current Model"""
        return self._model

    def fitModel(self, X:np.ndarray, y:np.ndarray) -> tf.keras.callbacks.History:
        """Fits the model to training data and saves the model to the checkpoint 
        path."""
        inputShape = len(X[0])
        self.createModel(inputShape)
    
        cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=self._checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)
        
        return self._model.fit(X, y,batch_size=len(X), epochs=self._epochs, validation_split=self._validation_split, callbacks=[cp_callback])

    def __str__(self) -> str:
        "RecL5N500"
        return "RecL" + str(self._layers) + "N" + str(self._layerSize)