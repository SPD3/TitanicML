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
        self.layerSize = layerSize
        self.layers = layers
        self.epochs = epochs
        self.validation_split = 0.1
        self.model = None
        self.learningRate = learningRate
        self.inputShape = None

    def createModel(self, inputShape:int) -> None:
        """Sets up connections between layers, creates and compiles a model"""
        self.inputShape = inputShape
        self.createInputsLinkedToOutputs()
        self.model = tf.keras.Model(inputs=self.inputs, outputs=self.outputs)
        self.compileModel()
        return self.model

    def createInputsLinkedToOutputs(self) -> None:
        """Sets up the layers between the input and output layers"""
        self.inputs = tf.keras.layers.Input(shape=(self.inputShape))
        x = tf.keras.layers.Dense(self.layerSize, activation="relu")(self.inputs)
        for i in range(self.layers - 1):
            x = tf.keras.layers.Dense(self.layerSize, activation="relu")(x)
        self.outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)
    
    def compileModel(self) -> None:
        """Compiles the model with the adam optimizer."""
        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(self.learningRate),
            loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
            metrics=["accuracy"]
        )
    
    def getModel(self):
        return self.model

    def fitModel(self, X:np.ndarray, y:np.ndarray) -> tf.keras.callbacks.History:
        """Fits the model to training data and saves the model to the checkpoint 
        path. Has a validation split of 0.1."""
        inputShape = len(X[0])
        self.createModel(inputShape)
    
        cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=self.checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)
        
        return self.model.fit(X, y,batch_size=len(X), epochs=self.epochs, validation_split=self.validation_split, callbacks=[cp_callback])
