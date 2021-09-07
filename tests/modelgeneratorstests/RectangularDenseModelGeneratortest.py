import unittest
from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
import tensorflow as tf
import os, glob
import numpy as np

class RectangularDenseModelGeneratorTest (unittest.TestCase):

    def setUp(self) -> None:
        self.name = "Test1"
        self.checkpoint_path = "./savedmodels/" + self.name + "cp.ckpt1"

    def testGetModel(self) -> None:
        """Makes sure that when a model is created, it can then be asked for"""
        simpleDenseModel = RectangularDenseModelGenerator(self.name)
        model = simpleDenseModel.getModel()
        self.assertEquals(model, None)

        simpleDenseModel.createModel(6)
        model = simpleDenseModel.getModel()
        self.assertTrue(issubclass(type(model), tf.keras.Model))

    def testCreateModel(self) -> None:
        """Makes sure that when a model is created each layer is a dense layer"""
        simpleDenseModel = RectangularDenseModelGenerator(self.name)
        model = simpleDenseModel.createModel(6)
        for i in range(1,len(model.layers)):
            self.assertTrue(issubclass(type(model.layers[i]), tf.keras.layers.Dense))

    def testCreateInputsLinkedToOutputs(self) -> None:
        """Makes sure that all of the layers in a simple dense model generator 
        are dense layers"""
        simpleDenseModel = RectangularDenseModelGenerator(self.name)
        simpleDenseModel.__inputShape = 6
        simpleDenseModel.__createInputsLinkedToOutputs()
        model = tf.keras.Model(inputs=simpleDenseModel.__inputs, outputs=simpleDenseModel.__outputs)
        self.assertEquals(type(model.layers[0]), tf.keras.layers.InputLayer)
        for i in range(1,len(model.layers)):
            self.assertTrue(issubclass(type(model.layers[i]), tf.keras.layers.Dense))
    
    def testCompileModel(self) -> None:
        """Makes sure that when the model is compiled no exceptions are thrown"""
        simpleDenseModel = RectangularDenseModelGenerator(self.name)
        simpleDenseModel.__inputShape = 6
        simpleDenseModel.__createInputsLinkedToOutputs()
        simpleDenseModel.__model = tf.keras.Model(inputs=simpleDenseModel.__inputs, outputs=simpleDenseModel.__outputs)
        try:
            simpleDenseModel.__compileModel()
        except:
            self.fail("Compile model threw an exception")
            
    def testFitModel(self) -> None:
        """Makes sure that fitModel trains and saves a model"""
        X = [
            [1,1,0],
            [1,0,1],
            [1,0,0],
            [0,1,1],
            [0,0,1],
            [1,1,0],
            [1,0,1],
            [1,0,0],
            [0,1,1],
            [0,0,1],
            [1,1,0],
            [1,0,1],
            [1,0,0],
            [0,1,1],
            [0,0,1],
        ]
        y = [1,1,1,0,0,1,1,1,0,0,1,1,1,0,0]
        
        for filename in glob.glob(self.checkpoint_path + "*"):
            os.remove(filename)

        numberOfLayers = 5
        neuronsPerLayer = 500
        
        simpleDenseModel = RectangularDenseModelGenerator(self.name, neuronsPerLayer, numberOfLayers, epochs=10, learningRate=1.0e-3)
        simpleDenseModel.fitModel(np.array(X), np.array(y))
        simpleDenseModel.__validation_split = 0.0
        model = simpleDenseModel.getModel()
        predictions = model.predict(np.array(X)).tolist()
        for i in range(len(y)):
            self.assertAlmostEquals(predictions[i][0], y[i], delta=0.1)

        newSimpleDenseModel = RectangularDenseModelGenerator(self.name, neuronsPerLayer, numberOfLayers)
        newSimpleDenseModel.createModel(3)
        newModel = newSimpleDenseModel.getModel()
        newModel.load_weights(self.checkpoint_path)
        newPredictions = newModel.predict(np.array(X)).tolist()
        self.assertEquals(newPredictions, predictions)