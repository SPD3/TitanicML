import unittest
from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
import tensorflow as tf
import os, glob
import numpy as np

class RectangularDenseModelGeneratorTest (unittest.TestCase):

    def testGetModel(self) -> None:
        """Makes sure that when a model is asked for it is created if one does 
        not already exist"""
        simpleDenseModel = RectangularDenseModelGenerator(6)
        model = simpleDenseModel.getModel()
        self.assertTrue(issubclass(type(model), tf.keras.Model))

    def testCreateModel(self) -> None:
        """Makes sure that when a model is created each layer is a dense layer"""
        simpleDenseModel = RectangularDenseModelGenerator(6)
        simpleDenseModel.createModel()
        for i in range(1,len(simpleDenseModel.model.layers)):
            self.assertTrue(issubclass(type(simpleDenseModel.model.layers[i]), tf.keras.layers.Dense))

    def testCreateInputsLinkedToOutputs(self) -> None:
        """Makes sure that all of the layers in a simple dense model generator 
        are dense layers"""
        simpleDenseModel = RectangularDenseModelGenerator(6)
        simpleDenseModel.createInputsLinkedToOutputs()
        model = tf.keras.Model(inputs=simpleDenseModel.inputs, outputs=simpleDenseModel.outputs)
        self.assertEquals(type(model.layers[0]), tf.keras.layers.InputLayer)
        for i in range(1,len(model.layers)):
            self.assertTrue(issubclass(type(model.layers[i]), tf.keras.layers.Dense))
    
    def testCompileModel(self) -> None:
        """Makes sure that when the model is compiled no exceptions are thrown"""
        simpleDenseModel = RectangularDenseModelGenerator(6)
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
        name = "Test1"
        checkpoint_path = "./savedmodels/" + name + "cp.ckpt1"
        for filename in glob.glob(checkpoint_path + "*"):
            os.remove(filename)

        numberOfLayers = 5
        neuronsPerLayer = 100
        
        simpleDenseModel = RectangularDenseModelGenerator(3, neuronsPerLayer, numberOfLayers)
        simpleDenseModel.fitModel(np.array(X), np.array(y), checkpoint_path)
        simpleDenseModel.validation_split = 0.0
        model = simpleDenseModel.getModel()
        predictions = model.predict(np.array(X)).tolist()
        for i in range(len(y)):
            self.assertAlmostEquals(predictions[i][0], y[i], delta=0.1)

        newSimpleDenseModel = RectangularDenseModelGenerator(3, neuronsPerLayer, numberOfLayers)
        newModel = newSimpleDenseModel.getModel()
        newModel.load_weights(checkpoint_path)
        newPredictions = newModel.predict(np.array(X)).tolist()
        self.assertEquals(newPredictions, predictions)