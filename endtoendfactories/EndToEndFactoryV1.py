from preprocessdata.DataPreProcessorWithVisitor import DataPreProcessorWithVisitor
from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
from datacategoryvisitors.CategorizedDataVisitor import CategorizedDataVisitor
from endtoendfactories.EndToEndFactoryBase import EndToEndFactoryBase
import numpy as np
from modelgenerators.ModelGeneratorBase import ModelGeneratorBase
from preprocessdata.PreProcessDataBase import PreProcessDataBase

class EndToEndFactoryV1 (EndToEndFactoryBase):
    """First version of an EndToEndFactory, will increase in version number as 
    models are generated with higher and higher scores on the test set."""

    instance = None
    def getInstance():
        """Gets the single instance of this singleton"""
        if(EndToEndFactoryV1.instance == None):
            EndToEndFactoryV1.instance = EndToEndFactoryV1()
        return EndToEndFactoryV1.instance

    def getPreProcessData(self, data:np.ndarray, dataIncludesLabels:bool) -> PreProcessDataBase:
        """Gets a dataPreprocessorWithVisitor with a CategorizedDataVisitor"""
        categorizedDataVisitor = CategorizedDataVisitor()
        dataPreProcessorWithVisitor = DataPreProcessorWithVisitor(data, dataIncludesLabels,categorizedDataVisitor)
        return dataPreProcessorWithVisitor

    def getModelGenerator(self, inputShape:int) -> ModelGeneratorBase:
        """Gets a RectangularDenseModelGenerator"""
        return RectangularDenseModelGenerator(inputShape)
