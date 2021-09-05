from typing import Dict, List
from preprocessdata.PreProcessDataBase import PreProcessDataBase
import numpy as np

class DataPreProcessorWithVisitor (PreProcessDataBase):
    
    def __init__(self, data, dataIncludesLabels, dataCategoryVisitor) -> None:
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
        return self.categoryDictionary

    def getProcessedData(self) -> List:
        if(not self.hasProcessedData):
            self.putDataIntoCategories()
            self.visitAllDataCategories()
            self.arrangeDataPerPassengerInXAndY()
            self.hasProcessedData = True
        return np.array(self.y), np.array(self.X)

    def putDataIntoCategories(self) -> None:
        for passenger in self.data:
            passengerValueIndex = 0 
            for key in self.categoryDictionary.keys():
                if(key == "Survived" and not self.dataIncludesLabels):
                    continue
                self.categoryDictionary[key].append(passenger[passengerValueIndex])
                passengerValueIndex+= 1

    def visitAllDataCategories(self) -> None:
        self.visitedCategoriesDictionary = {}
        self.visitedCategoriesDictionary["PassengerId"] = self.dataCategoryVisitor.visitPassengerId(self.categoryDictionary["PassengerId"])
        self.visitedCategoriesDictionary["Survived"] = self.dataCategoryVisitor.visitSurvived(self.categoryDictionary["Survived"])
        self.visitedCategoriesDictionary["Pclass"] = self.dataCategoryVisitor.visitPclass(self.categoryDictionary["Pclass"])
        self.visitedCategoriesDictionary["Name"] = self.dataCategoryVisitor.visitName(self.categoryDictionary["Name"])
        self.visitedCategoriesDictionary["Sex"] = self.dataCategoryVisitor.visitSex(self.categoryDictionary["Sex"])
        self.visitedCategoriesDictionary["Age"] = self.dataCategoryVisitor.visitAge(self.categoryDictionary["Age"])
        self.visitedCategoriesDictionary["SibSp"] = self.dataCategoryVisitor.visitSibSp(self.categoryDictionary["SibSp"])
        self.visitedCategoriesDictionary["Parch"] = self.dataCategoryVisitor.visitParch(self.categoryDictionary["Parch"])
        self.visitedCategoriesDictionary["Ticket"] = self.dataCategoryVisitor.visitTicket(self.categoryDictionary["Ticket"])
        self.visitedCategoriesDictionary["Fare"] = self.dataCategoryVisitor.visitFare(self.categoryDictionary["Fare"])
        self.visitedCategoriesDictionary["Cabin"] = self.dataCategoryVisitor.visitCabin(self.categoryDictionary["Cabin"])
        self.visitedCategoriesDictionary["Embarked"] = self.dataCategoryVisitor.visitEmbarked(self.categoryDictionary["Embarked"])

    def arrangeDataPerPassengerInXAndY(self) -> None:
        for label in self.visitedCategoriesDictionary["Survived"]:
            self.y.append(label[0])
        for i in range(len(self.data)):
            passenger = []
            for key in self.visitedCategoriesDictionary.keys():
                if(key == "Survived"):
                    continue
                for value in self.visitedCategoriesDictionary[key][i]:
                    passenger.append(value)
            self.X.append(passenger)