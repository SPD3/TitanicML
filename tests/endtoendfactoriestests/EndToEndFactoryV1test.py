from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
from endtoendfactories.EndToEndFactoryV1 import EndToEndFactoryV1
from preprocessdata.DataPreProcessorWithVisitor import DataPreProcessorWithVisitor
import unittest

class EndToEndFactoryV1Test (unittest.TestCase):
    """Tests the EndToEndFactoryV1 class"""
    def testGetPreProcessData(self) -> None:

        """Makes sure this end to end factory gives back a 
        DataPreprocessorWithVisitor"""
        data = [
            [1,2,3,4],
            [5,6,7,False]
        ]
        preProcessData = EndToEndFactoryV1.getInstance().getPreProcessData(data, True)
        self.assertTrue(issubclass(type(preProcessData), DataPreProcessorWithVisitor))

    def testGetModelGenerator(self) -> None:
        """Makes sure this end to end factory gives back a RectangularDenseModelGenerator"""
        modelGenerator = EndToEndFactoryV1.getInstance().getModelGenerator()
        self.assertTrue(issubclass(type(modelGenerator), RectangularDenseModelGenerator))