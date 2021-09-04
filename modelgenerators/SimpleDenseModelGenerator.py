from modelgenerators.ModelGeneratorBase import ModelGeneratorBase
import tensorflow as tf

class SimpleDenseModelGenerator (ModelGeneratorBase):

    def __init__(self, inputShape) -> None:
        super().__init__()
        self.layerSize = 256
        self.layers = 5
        self.epochs = 50
        self.inputShape = inputShape
        self.model = None

    def getModel(self):
        if(self.model == None):
            self.createModel()
        return self.model

    def createModel(self):
        self.createInputsLinkedToOutputs()
        self.model = tf.keras.Model(inputs=self.inputs, outputs=self.outputs)
        self.compileModel()

    def createInputsLinkedToOutputs(self):
        self.inputs = tf.keras.layers.Input(shape=(self.inputShape))
        x = tf.keras.layers.Dense(self.layerSize, activation="relu")(self.inputs)
        for i in range(self.layers):
            x = tf.keras.layers.Dense(self.layerSize, activation="relu")(x)
        self.outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)
    
    def compileModel(self):
        self.model.compile(
            optimizer='adam',
            loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
            metrics=["accuracy"]
        )

    def fitModel(self, X, y, checkpointPath):
        if(self.model == None):
            self.createModel()
    
        cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpointPath,
                                                 save_weights_only=True,
                                                 verbose=1)
        self.model.fit(X, y, epochs=self.epochs, validation_split=0.1, callbacks=[cp_callback])
