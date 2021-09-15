from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
from endtoendfactories.EndToEndFactoryV2 import EndToEndFactoryV2
from dataprocessors.DataProcessorGaussAndCosine import DataProcessorGaussAndCosine
import unittest

class EndToEndFactoryV2Test (unittest.TestCase):
    """Tests the EndToEndFactoryV2 class"""
    def testGetPreProcessData(self) -> None:
        """Makes sure this end to end factory gives back a 
        DataProcessorGaussAndCosine"""
        data = [
            [1,2,3,4],
            [5,6,7,False]
        ]
        preProcessData = EndToEndFactoryV2.getInstance().getPreProcessData(data, True)
        self.assertTrue(issubclass(type(preProcessData), DataProcessorGaussAndCosine))

    def testGetModelGenerator(self) -> None:
        """Makes sure this end to end factory gives back a RectangularDenseModelGenerator"""
        modelGenerator = EndToEndFactoryV2.getInstance().getModelGenerator()
        self.assertTrue(issubclass(type(modelGenerator), RectangularDenseModelGenerator))