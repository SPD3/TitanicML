from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase
from typing import Dict, List
from preprocessdata.PreProcessDataBase import PreProcessDataBase
import numpy as np

class DataPreProcessorWithVisitor (PreProcessDataBase):
    """Takes a DataCategoryVisitorBase and visits all the columns in the data to 
    process the data and prepare it for an ML algorithm"""
    
    def __init__(self, data:np.ndarray, dataIncludesLabels:bool, dataCategoryVisitor:DataCategoryVisitorBase) -> None:
        super().__init__(data, dataIncludesLabels)
        self.categoryDictionary = {
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
        self.hasProcessedData = False
        self.dataCategoryVisitor = dataCategoryVisitor

    def getCategoryDictionary(self) -> Dict:
        """Gets the category dictionary which has entries for each section of 
        information for every passenger"""
        return self.categoryDictionary

    def getProcessedData(self) -> tuple[np.ndarray, np.ndarray]:
        """Processes the data if it has not yet done so and then returns 
        y and X"""
        if(not self.hasProcessedData):
            self.putDataIntoCategories()
            self.visitAllDataCategories()
            self.arrangeDataPerPassengerInXAndY()
            self.hasProcessedData = True
        return np.array(self.y), np.array(self.X)

    def putDataIntoCategories(self) -> None:
        """Takes the data for each passenger and places it into the right 
        categories"""
        for passenger in self.data:
            passengerValueIndex = 0 
            for key in self.categoryDictionary.keys():
                if(key == "Survived" and not self.dataIncludesLabels):
                    continue
                self.categoryDictionary[key].append(passenger[passengerValueIndex])
                passengerValueIndex+= 1

    def visitAllDataCategories(self) -> None:
        """Visits all of the data categories and reassigns categoryDictionary 
        accordingly"""
        self.categoryDictionary["PassengerId"] = self.dataCategoryVisitor.visitPassengerId(self.categoryDictionary["PassengerId"])
        self.categoryDictionary["Survived"] = self.dataCategoryVisitor.visitSurvived(self.categoryDictionary["Survived"])
        self.categoryDictionary["Pclass"] = self.dataCategoryVisitor.visitPclass(self.categoryDictionary["Pclass"])
        self.categoryDictionary["Name"] = self.dataCategoryVisitor.visitName(self.categoryDictionary["Name"])
        self.categoryDictionary["Sex"] = self.dataCategoryVisitor.visitSex(self.categoryDictionary["Sex"])
        self.categoryDictionary["Age"] = self.dataCategoryVisitor.visitAge(self.categoryDictionary["Age"])
        self.categoryDictionary["SibSp"] = self.dataCategoryVisitor.visitSibSp(self.categoryDictionary["SibSp"])
        self.categoryDictionary["Parch"] = self.dataCategoryVisitor.visitParch(self.categoryDictionary["Parch"])
        self.categoryDictionary["Ticket"] = self.dataCategoryVisitor.visitTicket(self.categoryDictionary["Ticket"])
        self.categoryDictionary["Fare"] = self.dataCategoryVisitor.visitFare(self.categoryDictionary["Fare"])
        self.categoryDictionary["Cabin"] = self.dataCategoryVisitor.visitCabin(self.categoryDictionary["Cabin"])
        self.categoryDictionary["Embarked"] = self.dataCategoryVisitor.visitEmbarked(self.categoryDictionary["Embarked"])

    def arrangeDataPerPassengerInXAndY(self) -> None:
        """Arranges the data from categoryDictionary into X and y such that it 
        can be passed to the client in a format that can be easily used by an 
        ML algorithm"""
        for label in self.categoryDictionary["Survived"]:
            self.y.append(label[0])
        for i in range(len(self.data)):
            passenger = []
            for key in self.categoryDictionary.keys():
                if(key == "Survived"):
                    continue
                for value in self.categoryDictionary[key][i]:
                    passenger.append(value)
            self.X.append(passenger)