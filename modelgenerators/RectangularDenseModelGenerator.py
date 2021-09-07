from modelgenerators.ModelGeneratorBase import ModelGeneratorBase
import tensorflow as tf
import numpy as np

class RectangularDenseModelGenerator (ModelGeneratorBase):
    """Creates a NN with the same layersize for all layers specified"""

    def __init__(self, inputShape:int, name:str, layerSize:int=512, layers:int=10) -> None:
        """
        Arguments:
        -----------
        inputShape: the size of the input tensor
        layersize: the desired number of nodes for each layer
        layers: the desired number of layers between the input and sigmoid output layer
        """
        super().__init__(inputShape,name)
        self.layerSize = layerSize
        self.layers = layers
        self.epochs = 40
        self.validation_split = 0.1
        self.model = None
        self.learningRate = 5.0e-5
        
        #1.0e-5 fromlogits True, no activation
        #1.0e-6, fromlogits False, sigmoid activation

    def getModel(self) -> tf.keras.Model:
        """Creates a model if one hasn't been made yet and returns the model"""
        if(self.model == None):
            self.createModel()
        return self.model

    def createModel(self) -> None:
        """Sets up connections between layers, creates and compiles a model"""
        self.createInputsLinkedToOutputs()
        self.model = tf.keras.Model(inputs=self.inputs, outputs=self.outputs)
        self.compileModel()

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

    def fitModel(self, X:np.ndarray, y:np.ndarray) -> tf.keras.callbacks.History:
        """Fits the model to training data and saves the model to the checkpoint 
        path. Has a validation split of 0.1."""
        if(self.model == None):
            self.createModel()
    
        cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=self.checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)
        
        return self.model.fit(X, y,batch_size=len(X), epochs=self.epochs, validation_split=self.validation_split, callbacks=[cp_callback])
