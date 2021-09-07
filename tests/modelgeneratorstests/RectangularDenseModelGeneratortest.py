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
        """Makes sure that when a model is asked for it is created if one does 
        not already exist"""
        simpleDenseModel = RectangularDenseModelGenerator(self.name)
        model = simpleDenseModel.getModel(6)
        self.assertTrue(issubclass(type(model), tf.keras.Model))

    def testCreateModel(self) -> None:
        """Makes sure that when a model is created each layer is a dense layer"""
        simpleDenseModel = RectangularDenseModelGenerator(self.name)
        simpleDenseModel.createModel(6)
        for i in range(1,len(simpleDenseModel.model.layers)):
            self.assertTrue(issubclass(type(simpleDenseModel.model.layers[i]), tf.keras.layers.Dense))

    def testCreateInputsLinkedToOutputs(self) -> None:
        """Makes sure that all of the layers in a simple dense model generator 
        are dense layers"""
        simpleDenseModel = RectangularDenseModelGenerator(self.name)
        simpleDenseModel.inputShape = 6
        simpleDenseModel.createInputsLinkedToOutputs()
        model = tf.keras.Model(inputs=simpleDenseModel.inputs, outputs=simpleDenseModel.outputs)
        self.assertEquals(type(model.layers[0]), tf.keras.layers.InputLayer)
        for i in range(1,len(model.layers)):
            self.assertTrue(issubclass(type(model.layers[i]), tf.keras.layers.Dense))
    
    def testCompileModel(self) -> None:
        """Makes sure that when the model is compiled no exceptions are thrown"""
        simpleDenseModel = RectangularDenseModelGenerator(self.name)
        simpleDenseModel.inputShape = 6
        simpleDenseModel.createInputsLinkedToOutputs()
        simpleDenseModel.model = tf.keras.Model(inputs=simpleDenseModel.inputs, outputs=simpleDenseModel.outputs)
        try:
            simpleDenseModel.compileModel()
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
        neuronsPerLayer = 100
        
        simpleDenseModel = RectangularDenseModelGenerator(self.name, neuronsPerLayer, numberOfLayers)
        simpleDenseModel.fitModel(np.array(X), np.array(y))
        simpleDenseModel.validation_split = 0.0
        model = simpleDenseModel.getModel()
        predictions = model.predict(np.array(X)).tolist()
        for i in range(len(y)):
            self.assertAlmostEquals(predictions[i][0], y[i], delta=0.1)

        newSimpleDenseModel = RectangularDenseModelGenerator(3,self.name, neuronsPerLayer, numberOfLayers)
        newModel = newSimpleDenseModel.getModel()
        newModel.load_weights(self.checkpoint_path)
        newPredictions = newModel.predict(np.array(X)).tolist()
        self.assertEquals(newPredictions, predictions)