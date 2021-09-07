from preprocessdata.DataPreProcessorWithVisitor import DataPreProcessorWithVisitor
from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
from datacategoryvisitors.CategorizedDataVisitor import CategorizedDataVisitor
from endtoendfactories.EndToEndFactoryBase import EndToEndFactoryBase
import numpy as np
from modelgenerators.ModelGeneratorBase import ModelGeneratorBase
from preprocessdata.PreProcessDataBase import PreProcessDataBase

class EndToEndFactoryV1 (EndToEndFactoryBase):
    """First version of an EndToEndFactory, will increase in version number as 
    models are generated with higher and higher scores on the test set.
    """

    def __init__(self) -> None:
        self._name = "ModelV1"

    _instance = None
    def getInstance():
        """Gets the single instance of this singleton"""
        if(EndToEndFactoryV1._instance == None):
            EndToEndFactoryV1._instance = EndToEndFactoryV1()
        return EndToEndFactoryV1._instance

    def getPreProcessData(self, data:np.ndarray, dataIncludesLabels:bool) -> PreProcessDataBase:
        """Gets a dataPreprocessorWithVisitor with a CategorizedDataVisitor"""
        categorizedDataVisitor = CategorizedDataVisitor()
        dataPreProcessorWithVisitor = DataPreProcessorWithVisitor(data, dataIncludesLabels,categorizedDataVisitor)
        return dataPreProcessorWithVisitor

    def getModelGenerator(self, inputShape:int) -> ModelGeneratorBase:
        """Gets a RectangularDenseModelGenerator"""
        return RectangularDenseModelGenerator(inputShape, self._name)

    def getName(self) -> str:
        """Gets the name of this factory"""
        return self._name