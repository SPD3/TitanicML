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
from typing import List
from datacategoryvisitors.processeddatabuilders.DestroyDataBuilder \
    import DestroyDataBuilder
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase

class SimpleDataCategoryVisitor (DataCategoryVisitorBase):
    """This data category visitor prefers to scale data for a ML 
    algorithm as opposed to putting the data into bins"""

    def visitPassengerId(self, passengerId) -> List:
        builder = DestroyDataBuilder()
        return builder.getProcessedData(passengerId)

    def visitSurvived(self, survived) -> List:
        builder = NoModificationsToDataBuilder()
        return builder.getProcessedData(survived)

    def visitPclass(self, pClass) -> List:
        builder = ScaleDataBuilder(1.0/3.0)
        return builder.getProcessedData(pClass)

    def visitName(self, name) -> List:
        builder = NameClassifierBuilder()
        return builder.getProcessedData(name)

    def visitSex(self, sex) -> List:
        builder = BinarySexDataBuilder()
        return builder.getProcessedData(sex)

    def visitAge(self, age) -> List:
        builder = ScaleDataBuilder(1.0/80.0)
        return builder.getProcessedData(age)

    def visitSibSp(self, sibSp) -> List:
        builder = ScaleDataBuilder(1.0/8.0)
        return builder.getProcessedData(sibSp)

    def visitParch(self, parch) -> List:
        builder = ScaleDataBuilder(1.0/6.0)
        return builder.getProcessedData(parch)

    def visitTicket(self, ticket) -> List:
        builder = TicketClassifierBuilder()
        return builder.getProcessedData(ticket)

    def visitFare(self, fare) -> List:
        builder = ScaleDataBuilder(1.0/512.0)
        return builder.getProcessedData(fare)

    def visitCabin(self, cabin) -> List:
        builder = CabinClassifierBuilder()
        return builder.getProcessedData(cabin)

    def visitEmbarked(self, embarked) -> List:
        builder = PortOfEmbarkationBuilder()
        return builder.getProcessedData(embarked)