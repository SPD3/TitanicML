from __future__ import annotations
from dataprocessors.DataProcessorWithVisitor import DataProcessorWithVisitor
from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
from datacategoryvisitors.CategorizedDataVisitor import CategorizedDataVisitor
from endtoendfactories.EndToEndFactoryBase import EndToEndFactoryBase
import numpy as np

class EndToEndFactoryV1 (EndToEndFactoryBase):
    """First version of an EndToEndFactory, will increase in version number as 
    models are generated with higher and higher scores on the test set.
    """

    def __init__(self) -> None:
        self._name = "ModelV1"

    _instance = None
    def getInstance() -> EndToEndFactoryV1:
        """Gets the single instance of this singleton"""
        if(EndToEndFactoryV1._instance == None):
            EndToEndFactoryV1._instance = EndToEndFactoryV1()
        return EndToEndFactoryV1._instance

    def getPreProcessData(self, data:np.ndarray, dataIncludesLabels:bool) -> CategorizedDataVisitor:
        """Gets a dataPreprocessorWithVisitor with a CategorizedDataVisitor"""
        categorizedDataVisitor = CategorizedDataVisitor()
        dataProcessorWithVisitor = DataProcessorWithVisitor(data, dataIncludesLabels,categorizedDataVisitor)
        return dataProcessorWithVisitor

    def getModelGenerator(self) -> RectangularDenseModelGenerator:
        """Gets a RectangularDenseModelGenerator"""
        return RectangularDenseModelGenerator(self._name)

    def getName(self) -> str:
        """Gets the name of this factory"""
        return self._name