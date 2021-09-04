from preprocessdata.PreProcessDataBase import PreProcessDataBase
from modelgenerators.ModelGeneratorBase import ModelGeneratorBase
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase
from preprocessdata.DataPreProcessorWithVisitor import DataPreProcessorWithVisitor
from endtoendfactories.FactoryBase import FactoryBase
from preprocessdata.SimpleDataPreProcessor import SimpleDataPreProcessor
from modelgenerators.SimpleDenseModelGenerator import SimpleDenseModelGenerator
from datacategoryvisitors.SimpleDataCategoryVisitor import SimpleDataCategoryVisitor

class SimpleFactory (FactoryBase):

    instance = None
    def getInstance():
        if(SimpleFactory.instance == None):
            SimpleFactory.instance = SimpleFactory()
        return SimpleFactory.instance
            
    def getDataPreProcessor(self, data, dataIncludesLabels) -> PreProcessDataBase:
        return DataPreProcessorWithVisitor(data, dataIncludesLabels, self.getDataCategoryVisitor())

    def getModel(self, inputShape) -> ModelGeneratorBase:
        return SimpleDenseModelGenerator(inputShape)

    def getDataCategoryVisitor(self) -> DataCategoryVisitorBase:
        return SimpleDataCategoryVisitor()