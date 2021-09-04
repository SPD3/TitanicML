from endtoendfactories.FactoryBase import FactoryBase
from preprocessdata.SimpleDataPreProcessor import SimpleDataPreProcessor
from model.SimpleDenseModel import SimpleDenseModel

class SimpleFactory (FactoryBase):

    instance = None
    def getInstance():
        if(SimpleFactory.instance == None):
            SimpleFactory.instance = SimpleFactory()
        return SimpleFactory.instance
            
    def getDataPreProcessor(self):
        return SimpleDataPreProcessor

    def getModelType(self):
        return SimpleDenseModel