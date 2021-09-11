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
        """Destroys passengerID info, it is not important to an ML algorithm"""
        builder = DestroyDataBuilder()
        return builder.getProcessedData(passengerId)

    def visitSurvived(self, survived) -> list:
        """Does not modify the survived data at all"""
        builder = NoModificationsToDataBuilder()
        return builder.getProcessedData(survived)

    def visitPclass(self, pClass) -> list:
        """Scales the Pclass by a factor of 1/3"""
        builder = ScaleDataBuilder(1.0/3.0)
        return builder.getProcessedData(pClass)

    def visitName(self, name) -> list:
        """Categorizes names into bins"""
        builder = NameClassifierBuilder()
        return builder.getProcessedData(name)

    def visitSex(self, sex) -> list:
        """Turns sex from a string to a binary value for an ML algorithm"""
        builder = BinarySexDataBuilder()
        return builder.getProcessedData(sex)

    def visitAge(self, age) -> list:
        """Scales age by a factor of 1/80"""
        builder = ScaleDataBuilder(1.0/80.0)
        return builder.getProcessedData(age)

    def visitSibSp(self, sibSp) -> list:
        """Scales sibsp by a factor of 1/8"""
        builder = ScaleDataBuilder(1.0/8.0)
        return builder.getProcessedData(sibSp)

    def visitParch(self, parch) -> list:
        """Scales parch by a factor of 1/6"""
        builder = ScaleDataBuilder(1.0/6.0)
        return builder.getProcessedData(parch)

    def visitTicket(self, ticket) -> list:
        """Categorizes tickets into bins"""
        builder = TicketClassifierBuilder()
        return builder.getProcessedData(ticket)

    def visitFare(self, fare) -> list:
        """Scales Fare by a factor of 1/512"""
        builder = ScaleDataBuilder(1.0/512.0)
        return builder.getProcessedData(fare)

    def visitCabin(self, cabin) -> list:
        """Categorizes cabin names into bins"""
        builder = CabinClassifierBuilder()
        return builder.getProcessedData(cabin)

    def visitEmbarked(self, embarked) -> list:
        """Categorizes ports of embarkation into bins"""
        builder = PortOfEmbarkationBuilder()
        return builder.getProcessedData(embarked)

    def __str__(self) -> str:
        return "ScalVis"