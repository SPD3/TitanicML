from datacategoryvisitors.processeddatabuilders.ScaleDataBuilder import ScaleDataBuilder
from datacategoryvisitors.processeddatabuilders.NoModificationsToDataBuilder import NoModificationsToDataBuilder
from datacategoryvisitors.processeddatabuilders.BinarySexDataBuilder import BinarySexDataBuilder
from datacategoryvisitors.processeddatabuilders.ReplaceNanWithZeroBuilder import ReplaceNanWithZeroBuilder
from datacategoryvisitors.processeddatabuilders.CompositeDataBuilder import CompositeDataBuilder
from typing import List, Tuple
from datacategoryvisitors.processeddatabuilders.DestroyDataBuilder import DestroyDataBuilder
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase

class SimpleDataCategoryVisitor (DataCategoryVisitorBase):

    def visitPassengerId(self, passengerId) -> List:
        destroyDataBuilder = DestroyDataBuilder()
        return destroyDataBuilder.getProcessedData(passengerId)

    def visitSurvived(self, survived) -> List:
        noModificationsToDataBuilder = NoModificationsToDataBuilder()
        return noModificationsToDataBuilder.getProcessedData(survived)

    def visitPclass(self, pClass) -> List:
        scaleDataBuilder = ScaleDataBuilder(1.0/3.0)
        return scaleDataBuilder.getProcessedData(pClass)

    def visitName(self, name) -> List:
        destroyDataBuilder = DestroyDataBuilder()
        return destroyDataBuilder.getProcessedData(name)

    def visitSex(self, sex) -> List:
        binarySexDataBuilder = BinarySexDataBuilder()
        return binarySexDataBuilder.getProcessedData(sex)

    def visitAge(self, age) -> List:
        scaleDataBuilder = ScaleDataBuilder(1.0/100.0)
        replaceNanWithZeroBuilder = ReplaceNanWithZeroBuilder()
        composite = CompositeDataBuilder([replaceNanWithZeroBuilder, scaleDataBuilder])
        return composite.getProcessedData(age)

    def visitSibSp(self, sibSp) -> List:
        scaleDataBuilder = ScaleDataBuilder(1.0/8.0)
        return scaleDataBuilder.getProcessedData(sibSp)

    def visitParch(self, parch) -> List:
        scaleDataBuilder = ScaleDataBuilder(1.0/6.0)
        return scaleDataBuilder.getProcessedData(parch)

    def visitTicket(self, ticket) -> List:
        destroyDataBuilder = DestroyDataBuilder()
        return destroyDataBuilder.getProcessedData(ticket)

    def visitFare(self, fare) -> List:
        scaleDataBuilder = ScaleDataBuilder(1.0/512.0)
        return scaleDataBuilder.getProcessedData(fare)

    def visitCabin(self, cabin) -> List:
        destroyDataBuilder = DestroyDataBuilder()
        return destroyDataBuilder.getProcessedData(cabin)

    def visitEmbarked(self, embarked) -> List:
        destroyDataBuilder = DestroyDataBuilder()
        return destroyDataBuilder.getProcessedData(embarked)