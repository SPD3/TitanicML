from __future__ import annotations
from dataprocessors.DataProcessorGaussAndCosine import DataProcessorGaussAndCosine
from dataprocessors.DataProcessorWithVisitor import DataProcessorWithVisitor

import pandas as pd
from dataprocessors.DataProcessorGaussianKernel import DataProcessorGaussianKernel 
from dataprocessors.DataProcessorCombiner import DataProcessorCombiner 
from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
from datacategoryvisitors.ScaledDataCategoryVisitor import ScaledDataCategoryVisitor
from endtoendfactories.EndToEndFactoryBase import EndToEndFactoryBase
import numpy as np

class EndToEndFactoryV2 (EndToEndFactoryBase):
    """First version of an EndToEndFactory, will increase in version number as 
    models are generated with higher and higher scores on the test set.
    """

    def __init__(self) -> None:
        self._name = "V2"

    _instance = None
    def getInstance() -> EndToEndFactoryV2:
        """Gets the single instance of this singleton"""
        if(EndToEndFactoryV2._instance == None):
            EndToEndFactoryV2._instance = EndToEndFactoryV2()
        return EndToEndFactoryV2._instance

    def getPreProcessData(self, data:np.ndarray, dataIncludesLabels:bool) -> DataProcessorWithVisitor:
        """Gets a dataPreprocessorWithVisitor with a CategorizedDataVisitor"""
        scaledDataCategoryVisitor = ScaledDataCategoryVisitor()
        train_data = pd.read_csv("titanic/train.csv")
        train_data = train_data.to_numpy().tolist()
        dataProcessorWithVisitor = DataProcessorWithVisitor(train_data, True, scaledDataCategoryVisitor)
        _, dataToCompareTo = dataProcessorWithVisitor.getProcessedData()
        
        dataProcessor = DataProcessorGaussAndCosine(data, dataIncludesLabels, dataCategoryVisitor=scaledDataCategoryVisitor, sigma=1.0, dataToCompareTo=dataToCompareTo)
        return dataProcessor

    def getModelGenerator(self) -> RectangularDenseModelGenerator:
        """Gets a RectangularDenseModelGenerator"""
        return RectangularDenseModelGenerator(self._name, layerSize=1024, layers=10, epochs=120)

    def getName(self) -> str:
        """Gets the name of this factory"""
        return self._name