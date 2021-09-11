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
from datacategoryvisitors.processeddatabuilders.DestroyDataBuilder \
    import DestroyDataBuilder
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase

class CategorizedDataVisitor (DataCategoryVisitorBase):
    """This data category visitor prefers to put the data into bins for a ML 
    algorithm as opposed to scaling the data"""

    def visitPassengerId(self, passengerId:list[int]) -> list[list[float]]:
        """Destroys passengerID info, it is not important to an ML algorithm"""
        builder = DestroyDataBuilder()
        return builder.getProcessedData(passengerId)

    def visitSurvived(self, survived:list[int]) -> list[list[float]]:
        """Does not modify the survived data at all"""
        builder = NoModificationsToDataBuilder()
        return builder.getProcessedData(survived)

    def visitPclass(self, pClass:list[int]) -> list[list[float]]:
        """Categorizes pclass into three different bins: 1,2,3"""
        builder = DataCategorizerBuilder([1.0,2.0,3.0])
        return builder.getProcessedData(pClass)

    def visitName(self, name:list[str]) -> list[list[float]]:
        """Categorizes names into bins"""
        builder = NameClassifierBuilder()
        return builder.getProcessedData(name)

    def visitSex(self, sex:list[str]) -> list[list[float]]:
        """Turns sex from a string to a binary value for an ML algorithm"""
        binarySexDataBuilder = BinarySexDataBuilder()
        return binarySexDataBuilder.getProcessedData(sex)

    def visitAge(self, age:list[float]) -> list[list[float]]:
        """Categorizes ages into bins"""
        builder = AgeClassifierBuilder()
        return builder.getProcessedData(age)

    def visitSibSp(self, sibSp:list[int]) -> list[list[float]]:
        """Categorizes sibsp into 9 different bins: 0-8"""
        builder = DataCategorizerBuilder([0,1,2,3,4,5,6,7,8])
        return builder.getProcessedData(sibSp)

    def visitParch(self, parch:list[int]) -> list[list[float]]:
        """Categorizes parch into 7 different bins: 0-6"""
        builder = DataCategorizerBuilder([0,1,2,3,4,5,6])
        return builder.getProcessedData(parch)

    def visitTicket(self, ticket:list) -> list[list[float]]:
        """Categorizes tickets into bins"""
        builder = TicketClassifierBuilder()
        return builder.getProcessedData(ticket)

    def visitFare(self, fare:list[float]) -> list[list[float]]:
        """Categorizes fares into 6 different bins"""
        builder = DataCategorizerBuilder([12,25,50,100,200,500])
        return builder.getProcessedData(fare)
    
    def visitCabin(self, cabin:list) -> list[list[float]]:
        """Categorizes cabin names into bins"""
        builder = CabinClassifierBuilder()
        return builder.getProcessedData(cabin)

    def visitEmbarked(self, embarked:list[str]) -> list[list[float]]:
        """Categorizes ports of embarkation into bins"""
        builder = PortOfEmbarkationBuilder()
        return builder.getProcessedData(embarked)

    def __str__(self) -> str:
        return "CatVis"