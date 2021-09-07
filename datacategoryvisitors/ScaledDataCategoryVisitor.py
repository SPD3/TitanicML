from datacategoryvisitors.processeddatabuilders.PortOfEmbarkationBuilder \
    import PortOfEmbarkationBuilder
from datacategoryvisitors.processeddatabuilders.CabinClassifierBuilder \
    import CabinClassifierBuilder
from datacategoryvisitors.processeddatabuilders.TicketClassifierBuilder \
    import TicketClassifierBuilder
from datacategoryvisitors.processeddatabuilders.NameClassifierBuilder \
    import NameClassifierBuilder
from datacategoryvisitors.processeddatabuilders.AgeClassifierBuilder \
    import AgeClassifierBuilder
from datacategoryvisitors.processeddatabuilders.ScaleDataBuilder \
    import ScaleDataBuilder
from datacategoryvisitors.processeddatabuilders.NoModificationsToDataBuilder \
    import NoModificationsToDataBuilder
from datacategoryvisitors.processeddatabuilders.BinarySexDataBuilder \
    import BinarySexDataBuilder
from datacategoryvisitors.processeddatabuilders.DestroyDataBuilder \
    import DestroyDataBuilder
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase

class ScaledDataCategoryVisitor (DataCategoryVisitorBase):
    """This data category visitor prefers to scale data for a ML 
    algorithm as opposed to putting the data into bins"""

    def visitPassengerId(self, passengerId) -> list:
        builder = DestroyDataBuilder()
        return builder.getProcessedData(passengerId)

    def visitSurvived(self, survived) -> list:
        builder = NoModificationsToDataBuilder()
        return builder.getProcessedData(survived)

    def visitPclass(self, pClass) -> list:
        builder = ScaleDataBuilder(1.0/3.0)
        return builder.getProcessedData(pClass)

    def visitName(self, name) -> list:
        builder = NameClassifierBuilder()
        return builder.getProcessedData(name)

    def visitSex(self, sex) -> list:
        builder = BinarySexDataBuilder()
        return builder.getProcessedData(sex)

    def visitAge(self, age) -> list:
        builder = ScaleDataBuilder(1.0/80.0)
        return builder.getProcessedData(age)

    def visitSibSp(self, sibSp) -> list:
        builder = ScaleDataBuilder(1.0/8.0)
        return builder.getProcessedData(sibSp)

    def visitParch(self, parch) -> list:
        builder = ScaleDataBuilder(1.0/6.0)
        return builder.getProcessedData(parch)

    def visitTicket(self, ticket) -> list:
        builder = TicketClassifierBuilder()
        return builder.getProcessedData(ticket)

    def visitFare(self, fare) -> list:
        builder = ScaleDataBuilder(1.0/512.0)
        return builder.getProcessedData(fare)

    def visitCabin(self, cabin) -> list:
        builder = CabinClassifierBuilder()
        return builder.getProcessedData(cabin)

    def visitEmbarked(self, embarked) -> list:
        builder = PortOfEmbarkationBuilder()
        return builder.getProcessedData(embarked)

    def __str__(self) -> str:
        return "ScalVis"