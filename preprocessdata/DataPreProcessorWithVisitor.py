from datacategoryvisitors.CategorizedDataVisitor import CategorizedDataVisitor
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase
from typing import Dict
from preprocessdata.PreProcessDataBase import PreProcessDataBase
import numpy as np

class DataPreProcessorWithVisitor (PreProcessDataBase):
    """Takes a DataCategoryVisitorBase and visits all the columns in the data to 
    process the data and prepare it for an ML algorithm"""
    
    def __init__(self, data:np.ndarray, dataIncludesLabels:bool, dataCategoryVisitor:DataCategoryVisitorBase=CategorizedDataVisitor()) -> None:
        super().__init__(data, dataIncludesLabels)
        self._categoryDictionary = {
            "PassengerId" : [],
            "Survived" : [],
            "Pclass" : [],
            "Name" : [],
            "Sex" : [],
            "Age" : [],
            "SibSp" : [],
            "Parch" : [],
            "Ticket" : [],
            "Fare" : [],
            "Cabin" : [],
            "Embarked" : [],
        }
        self._hasProcessedData = False
        self._dataCategoryVisitor = dataCategoryVisitor

    def setDataCategoryVisitor(self, dataCategoryVisitor):
        """Sets the _dataCategoryVisitor to _dataCategoryVisitor"""
        self._dataCategoryVisitor = dataCategoryVisitor

    def getCategoryDictionary(self) -> Dict:
        """Gets the category dictionary which has entries for each section of 
        information for every passenger"""
        return self._categoryDictionary

    def getProcessedData(self) -> tuple[np.ndarray, np.ndarray]:
        """Processes the data if it has not yet done so and then returns 
        y and X"""
        if(not self._hasProcessedData):
            self._putDataIntoCategories()
            self._visitAllDataCategories()
            self._arrangeDataPerPassengerInXAndY()
            self._hasProcessedData = True
        return np.array(self._y), np.array(self._X)

    def _putDataIntoCategories(self) -> None:
        """Takes the data for each passenger and places it into the right 
        categories"""
        for passenger in self._data:
            passengerValueIndex = 0 
            for key in self._categoryDictionary.keys():
                if(key == "Survived" and not self._dataIncludesLabels):
                    continue
                self._categoryDictionary[key].append(passenger[passengerValueIndex])
                passengerValueIndex+= 1

    def _visitAllDataCategories(self) -> None:
        """Visits all of the data categories and reassigns categoryDictionary 
        accordingly"""
        self._categoryDictionary["PassengerId"] = self._dataCategoryVisitor.visitPassengerId(self._categoryDictionary["PassengerId"])
        self._categoryDictionary["Survived"] = self._dataCategoryVisitor.visitSurvived(self._categoryDictionary["Survived"])
        self._categoryDictionary["Pclass"] = self._dataCategoryVisitor.visitPclass(self._categoryDictionary["Pclass"])
        self._categoryDictionary["Name"] = self._dataCategoryVisitor.visitName(self._categoryDictionary["Name"])
        self._categoryDictionary["Sex"] = self._dataCategoryVisitor.visitSex(self._categoryDictionary["Sex"])
        self._categoryDictionary["Age"] = self._dataCategoryVisitor.visitAge(self._categoryDictionary["Age"])
        self._categoryDictionary["SibSp"] = self._dataCategoryVisitor.visitSibSp(self._categoryDictionary["SibSp"])
        self._categoryDictionary["Parch"] = self._dataCategoryVisitor.visitParch(self._categoryDictionary["Parch"])
        self._categoryDictionary["Ticket"] = self._dataCategoryVisitor.visitTicket(self._categoryDictionary["Ticket"])
        self._categoryDictionary["Fare"] = self._dataCategoryVisitor.visitFare(self._categoryDictionary["Fare"])
        self._categoryDictionary["Cabin"] = self._dataCategoryVisitor.visitCabin(self._categoryDictionary["Cabin"])
        self._categoryDictionary["Embarked"] = self._dataCategoryVisitor.visitEmbarked(self._categoryDictionary["Embarked"])

    def _arrangeDataPerPassengerInXAndY(self) -> None:
        """Arranges the data from categoryDictionary into X and y such that it 
        can be passed to the client in a format that can be easily used by an 
        ML algorithm"""
        for label in self._categoryDictionary["Survived"]:
            self._y.append(label[0])
        for i in range(len(self._data)):
            passenger = []
            for key in self._categoryDictionary.keys():
                if(key == "Survived"):
                    continue
                for value in self._categoryDictionary[key][i]:
                    passenger.append(value)
            self._X.append(passenger)