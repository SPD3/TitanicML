from abc import ABC, abstractmethod

class DataCategoryVisitorBase (ABC):

    @abstractmethod
    def visitPassengerId(self, passengerId):
        pass

    @abstractmethod
    def visitSurvived(self, survived):
        pass

    @abstractmethod
    def visitPclass(self, pClass):
        pass

    @abstractmethod
    def visitName(self, name):
        pass

    @abstractmethod
    def visitSex(self, sex):
        pass

    @abstractmethod
    def visitAge(self, age):
        pass

    @abstractmethod
    def visitSibSp(self, sibSp):
        pass

    @abstractmethod
    def visitParch(self, parch):
        pass

    @abstractmethod
    def visitTicket(self, ticket):
        pass

    @abstractmethod
    def visitFare(self, fare):
        pass

    @abstractmethod
    def visitCabin(self, cabin):
        pass

    @abstractmethod
    def visitEmbarked(self, embarked):
        pass