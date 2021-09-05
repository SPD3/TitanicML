from datacategoryvisitors.processeddatabuilders.AgeClassifierBuilder \
    import AgeClassifierBuilder
from datacategoryvisitors.processeddatabuilders.TicketClassifierBuilder \
    import TicketClassifierBuilder
from datacategoryvisitors.processeddatabuilders.NameClassifierBuilder \
    import NameClassifierBuilder
from datacategoryvisitors.processeddatabuilders.CabinClassifierBuilder \
    import CabinClassifierBuilder
from datacategoryvisitors.processeddatabuilders.PortOfEmbarkationBuilder \
    import PortOfEmbarkationBuilder
from datacategoryvisitors.processeddatabuilders.DataCategorizerBuilder \
    import DataCategorizerBuilder
from datacategoryvisitors.processeddatabuilders.ScaleDataBuilder \
    import ScaleDataBuilder
from datacategoryvisitors.processeddatabuilders.NoModificationsToDataBuilder \
    import NoModificationsToDataBuilder
from datacategoryvisitors.processeddatabuilders.BinarySexDataBuilder \
    import BinarySexDataBuilder
from typing import List
from datacategoryvisitors.processeddatabuilders.DestroyDataBuilder \
    import DestroyDataBuilder
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase

class CategorizedDataVisitor (DataCategoryVisitorBase):
    """This data category visitor prefers to put the data into bins for a ML 
    algorithm as opposed to scaling the data"""

    def visitPassengerId(self, passengerId:List[int]) -> List[List[float]]:
        builder = DestroyDataBuilder()
        return builder.getProcessedData(passengerId)

    def visitSurvived(self, survived:List[int]) -> List[List[float]]:
        builder = NoModificationsToDataBuilder()
        return builder.getProcessedData(survived)

    def visitPclass(self, pClass:List[int]) -> List[List[float]]:
        builder = DataCategorizerBuilder([1.0,2.0,3.0])
        return builder.getProcessedData(pClass)

    def visitName(self, name:List[str]) -> List[List[float]]:
        builder = NameClassifierBuilder()
        return builder.getProcessedData(name)

    def visitSex(self, sex:List[str]) -> List[List[float]]:
        binarySexDataBuilder = BinarySexDataBuilder()
        return binarySexDataBuilder.getProcessedData(sex)

    def visitAge(self, age:List[float]) -> List[List[float]]:
        builder = AgeClassifierBuilder()
        return builder.getProcessedData(age)

    def visitSibSp(self, sibSp:List[int]) -> List[List[float]]:
        builder = DataCategorizerBuilder([0,1,2,3,4,5,6,7,8])
        return builder.getProcessedData(sibSp)

    def visitParch(self, parch:List[int]) -> List[List[float]]:
        builder = DataCategorizerBuilder([0,1,2,3,4,5,6])
        return builder.getProcessedData(parch)

    def visitTicket(self, ticket:List) -> List[List[float]]:
        builder = TicketClassifierBuilder()
        return builder.getProcessedData(ticket)

    def visitFare(self, fare:List[float]) -> List[List[float]]:
        scaleDataBuilder = ScaleDataBuilder(1.0/512.0)
        return scaleDataBuilder.getProcessedData(fare)
    
    def visitCabin(self, cabin:List) -> List[List[float]]:
        builder = CabinClassifierBuilder()
        return builder.getProcessedData(cabin)

    def visitEmbarked(self, embarked:List[str]) -> List[List[float]]:
        builder = PortOfEmbarkationBuilder()
        return builder.getProcessedData(embarked)