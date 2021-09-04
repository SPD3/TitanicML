from endtoendfactories.FactoryBase import FactoryBase
from preprocessdata.SimpleDataPreProcessor import SimpleDataPreProcessor

class SimpleFactory (FactoryBase):

    instance = None
    def getInstance():
        if(SimpleFactory.instance == None):
            SimpleFactory.instance = SimpleFactory()
        return SimpleFactory.instance
            
    def getDataPreProcessor(self):
        return SimpleDataPreProcessor