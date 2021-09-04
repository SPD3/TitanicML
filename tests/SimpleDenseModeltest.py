import unittest
from modelgenerators.SimpleDenseModelGenerator import SimpleDenseModelGenerator
import tensorflow as tf

class SimpleDenseModeltest (unittest.TestCase):

    def test_createInputsLinkedToOutputs(self):
        simpleDenseModel = SimpleDenseModelGenerator(6)
        simpleDenseModel.createInputsLinkedToOutputs()
        model = tf.keras.Model(inputs=simpleDenseModel.inputs, outputs=simpleDenseModel.outputs)
        self.assertEquals(type(model.layers[0]), tf.keras.layers.InputLayer)
        for i in range(1,len(model.layers)):
            self.assertEquals(type(model.layers[i]), tf.keras.layers.Dense)