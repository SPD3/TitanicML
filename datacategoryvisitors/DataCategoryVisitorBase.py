from abc import ABC, abstractmethod

class DataCategoryVisitorBase (ABC):
    """This is a visitor base class that specifies the way in which the data for 
    each passenger can be numerically represented for a ML algorithm"""

    @abstractmethod
    def visitPassengerId(self, passengerId:list[int]) -> list[list[float]]:
        pass

    @abstractmethod
    def visitSurvived(self, survived:list[int]) -> list[list[float]]:
        pass

    @abstractmethod
    def visitPclass(self, pClass:list[int]) -> list[list[float]]:
        pass

    @abstractmethod
    def visitName(self, name:list[str]) -> list[list[float]]:
        pass

    @abstractmethod
    def visitSex(self, sex:list[str]) -> list[list[float]]:
        pass

    @abstractmethod
    def visitAge(self, age:list[float]) -> list[list[float]]:
        pass

    @abstractmethod
    def visitSibSp(self, sibSp:list[int]) -> list[list[float]]:
        pass

    @abstractmethod
    def visitParch(self, parch:list[int]) -> list[list[float]]:
        pass

    @abstractmethod
    def visitTicket(self, ticket:list) -> list[list[float]]:
        pass

    @abstractmethod
    def visitFare(self, fare:list[float]) -> list[list[float]]:
        pass

    @abstractmethod
    def visitCabin(self, cabin:list) -> list[list[float]]:
        pass

    @abstractmethod
    def visitEmbarked(self, embarked:list[str]) -> list[list[float]]:
        pass