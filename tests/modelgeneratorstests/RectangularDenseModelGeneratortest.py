import unittest
from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
import tensorflow as tf
import os, glob
import numpy as np

class RectangularDenseModelGeneratorTest (unittest.TestCase):
    """Tests for the RectangularDenseModelGenerator class"""

    def setUp(self) -> None:
        self._name = "Test1"
        self._checkpoint_path = "./savedmodels/" + self._name + "cp.ckpt1"

    def testGetModel(self) -> None:
        """Makes sure that when a model is created, it can then be asked for"""
        simpleDenseModel = RectangularDenseModelGenerator(self._name)
        model = simpleDenseModel.getModel()
        self.assertEquals(model, None)

        simpleDenseModel.createModel(6)
        model = simpleDenseModel.getModel()
        self.assertTrue(issubclass(type(model), tf.keras.Model))

    def testCreateModel(self) -> None:
        """Makes sure that when a model is created each layer is a dense layer"""
        simpleDenseModel = RectangularDenseModelGenerator(self._name)
        model = simpleDenseModel.createModel(6)
        for i in range(1,len(model.layers)):
            self.assertTrue(issubclass(type(model.layers[i]), tf.keras.layers.Dense))

    def testCreateInputsLinkedToOutputs(self) -> None:
        """Makes sure that all of the layers in a simple dense model generator 
        are dense layers"""
        simpleDenseModel = RectangularDenseModelGenerator(self._name)
        simpleDenseModel._inputShape = 6
        simpleDenseModel._createInputsLinkedToOutputs()
        model = tf.keras.Model(inputs=simpleDenseModel._inputs, outputs=simpleDenseModel._outputs)
        self.assertEquals(type(model.layers[0]), tf.keras.layers.InputLayer)
        for i in range(1,len(model.layers)):
            self.assertTrue(issubclass(type(model.layers[i]), tf.keras.layers.Dense))
    
    def testCompileModel(self) -> None:
        """Makes sure that when the model is compiled no exceptions are thrown"""
        simpleDenseModel = RectangularDenseModelGenerator(self._name)
        simpleDenseModel._inputShape = 6
        simpleDenseModel._createInputsLinkedToOutputs()
        simpleDenseModel._model = tf.keras.Model(inputs=simpleDenseModel._inputs, outputs=simpleDenseModel._outputs)
        try:
            simpleDenseModel._compileModel()
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
        
        for filename in glob.glob(self._checkpoint_path + "*"):
            os.remove(filename)

        numberOfLayers = 5
        neuronsPerLayer = 500
        
        simpleDenseModel = RectangularDenseModelGenerator(self._name, neuronsPerLayer, numberOfLayers, epochs=10, learningRate=1.0e-3)
        simpleDenseModel._validation_split = 0.0
        simpleDenseModel.fitModel(np.array(X), np.array(y))
        model = simpleDenseModel.getModel()
        predictions = model.predict(np.array(X)).tolist()
        for i in range(len(y)):
            self.assertAlmostEquals(predictions[i][0], y[i], delta=0.1)

        newSimpleDenseModel = RectangularDenseModelGenerator(self._name, neuronsPerLayer, numberOfLayers)
        newSimpleDenseModel.createModel(3)
        newModel = newSimpleDenseModel.getModel()
        newModel.load_weights(self._checkpoint_path)
        newPredictions = newModel.predict(np.array(X)).tolist()
        self.assertEquals(newPredictions, predictions)

    def testString(self) -> None:
        """Tests the string representation of RectangularDenseModelGenerator"""     
        numberOfLayers = 5
        neuronsPerLayer = 500
        simpleDenseModel = RectangularDenseModelGenerator(self._name, neuronsPerLayer, numberOfLayers, epochs=10, learningRate=1.0e-3)
        self.assertEquals(str(simpleDenseModel), "RecL5N500VS0.1")

    def testModelGeneratorInitWithoutName(self) -> None:
        """Makes sure that a modelGenerator can be created without a name and 
        still operates correctly"""
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

        numberOfLayers = 5
        neuronsPerLayer = 500
        
        simpleDenseModel = RectangularDenseModelGenerator(layerSize=neuronsPerLayer, layers=numberOfLayers, epochs=10, learningRate=1.0e-3)
        simpleDenseModel._validation_split = 0.0
        simpleDenseModel.fitModel(np.array(X), np.array(y))
        model = simpleDenseModel.getModel()
        predictions = model.predict(np.array(X)).tolist()
        for i in range(len(y)):
            self.assertAlmostEquals(predictions[i][0], y[i], delta=0.1)