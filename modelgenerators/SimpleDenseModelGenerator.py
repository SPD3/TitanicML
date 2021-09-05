from modelgenerators.ModelGeneratorBase import ModelGeneratorBase
import tensorflow as tf

class SimpleDenseModelGenerator (ModelGeneratorBase):

    def __init__(self, inputShape, layersize=2056, layers = 5) -> None:
        super().__init__()
        self.layerSize = layersize
        self.layers = layers
        self.epochs = 30
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
        dropoutRate = 0.25
        x = tf.keras.layers.Dropout(dropoutRate)(x)
        for i in range(self.layers):
            x = tf.keras.layers.Dense(self.layerSize, activation="relu")(x)
            x = tf.keras.layers.Dropout(dropoutRate)(x)
        self.outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)
    
    def compileModel(self):
        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
            loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
            metrics=["accuracy"]
        )

    def fitModel(self, X, y, checkpointPath):
        if(self.model == None):
            self.createModel()
    
        cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpointPath,
                                                 save_weights_only=True,
                                                 verbose=1)
        
        self.model.fit(X, y, epochs=self.epochs, validation_split=0.0, callbacks=[cp_callback])
