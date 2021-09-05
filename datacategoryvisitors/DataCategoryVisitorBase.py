from abc import ABC, abstractmethod
from typing import List

class DataCategoryVisitorBase (ABC):
    """This is a visitor base class that specifies the way in which the data for 
    each passenger can be numerically represented for a ML algorithm"""

    @abstractmethod
    def visitPassengerId(self, passengerId:List[int]) -> List[List[float]]:
        pass

    @abstractmethod
    def visitSurvived(self, survived:List[int]) -> List[List[float]]:
        pass

    @abstractmethod
    def visitPclass(self, pClass:List[int]) -> List[List[float]]:
        pass

    @abstractmethod
    def visitName(self, name:List[str]) -> List[List[float]]:
        pass

    @abstractmethod
    def visitSex(self, sex:List[str]) -> List[List[float]]:
        pass

    @abstractmethod
    def visitAge(self, age:List[float]) -> List[List[float]]:
        pass

    @abstractmethod
    def visitSibSp(self, sibSp:List[int]) -> List[List[float]]:
        pass

    @abstractmethod
    def visitParch(self, parch:List[int]) -> List[List[float]]:
        pass

    @abstractmethod
    def visitTicket(self, ticket:List) -> List[List[float]]:
        pass

    @abstractmethod
    def visitFare(self, fare:List[float]) -> List[List[float]]:
        pass

    @abstractmethod
    def visitCabin(self, cabin:List) -> List[List[float]]:
        pass

    @abstractmethod
    def visitEmbarked(self, embarked:List[str]) -> List[List[float]]:
        pass