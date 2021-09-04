from endtoendfactories.FactoryBase import FactoryBase
from preprocessdata.SimpleDataPreProcessor import SimpleDataPreProcessor
from modelgenerators.SimpleDenseModelGenerator import SimpleDenseModelGenerator

class SimpleFactory (FactoryBase):

    instance = None
    def getInstance():
        if(SimpleFactory.instance == None):
            SimpleFactory.instance = SimpleFactory()
        return SimpleFactory.instance
            
    def getDataPreProcessorType(self):
        return SimpleDataPreProcessor

    def getModelType(self):
        return SimpleDenseModelGenerator