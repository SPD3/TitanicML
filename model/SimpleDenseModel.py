from model.ModelBase import ModelBase
import tensorflow as tf

class SimpleDenseModel (ModelBase):

    def __init__(self, inputShape) -> None:
        super().__init__()
        self.layerSize = 2056
        self.layers = 5
        self.inputShape = inputShape

    def createModel(self):
        self.createInputsLinkedToOutputs()
        self.model = tf.keras.Model(inputs=self.inputs, outputs=self.outputs)
        self.compileModel()
        return self.model

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
