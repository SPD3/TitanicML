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
        self.__layerSize = layerSize
        self.__layers = layers
        self.__epochs = epochs
        self.__validation_split = 0.1
        self.__model = None
        self.__learningRate = learningRate
        self.__inputShape = None

    def createModel(self, inputShape:int) -> tf.keras.Model:
        """Sets up connections between layers, creates and compiles a model"""
        self.__inputShape = inputShape
        self.__createInputsLinkedToOutputs()
        self.__model = tf.keras.Model(inputs=self.__inputs, outputs=self.__outputs)
        self.__compileModel()
        return self.__model

    def __createInputsLinkedToOutputs(self) -> None:
        """Sets up the layers between the input and output layers"""
        self.__inputs = tf.keras.layers.Input(shape=(self.__inputShape))
        x = tf.keras.layers.Dense(self.__layerSize, activation="relu")(self.__inputs)
        for i in range(self.__layers - 1):
            x = tf.keras.layers.Dense(self.__layerSize, activation="relu")(x)
        self.__outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)
    
    def __compileModel(self) -> None:
        """Compiles the model with the adam optimizer."""
        self.__model.compile(
            optimizer=tf.keras.optimizers.Adam(self.__learningRate),
            loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
            metrics=["accuracy"]
        )
    
    def getModel(self) -> tf.keras.Model:
        """Gets the current Model"""
        return self.__model

    def fitModel(self, X:np.ndarray, y:np.ndarray) -> tf.keras.callbacks.History:
        """Fits the model to training data and saves the model to the checkpoint 
        path."""
        inputShape = len(X[0])
        self.createModel(inputShape)
    
        cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=self._checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)
        
        return self.__model.fit(X, y,batch_size=len(X), epochs=self.__epochs, validation_split=self.__validation_split, callbacks=[cp_callback])
