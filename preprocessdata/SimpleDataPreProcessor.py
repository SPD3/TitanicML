from preprocessdata.PreProcessDataBase import PreProcessDataBase
import pandas as pd
import numpy as np

class SimpleDataPreProcessor (PreProcessDataBase):
    """First data attempt at processing data. This code is deprecated and 
    DataPreProcessorWithVisitor Should be used instead"""

    def __init__(self, data:np.ndarray, dataIncludesLabels:bool=True) -> None:
        super().__init__(data, dataIncludesLabels)
        self.dataIsProcessed = False

    def getProcessedData(self) -> tuple[np.ndarray, np.ndarray]:
        """Processed the data if it has not been yet and then returns y and X"""
        if(not self.dataIsProcessed):
            self.processData()
        return np.array(self.y), np.array(self.X)

    def processData(self) -> None:
        """Processes the data. Eliminates useless data, and relabels useful data
         in ways that a ML algorithm can use"""
        self.eliminateFirstColumnInTrainData()
        if(self.dataIncludesLabels):
            self.seperateLabelsFromData()
        else:
            self.createXAndMockLabels()
        self.scaleValuesInX()
        self.elinateUneccessaryValuesInX()
        self.replaceNans()
        self.dataIsProcessed = True

    def eliminateFirstColumnInTrainData(self) -> None:
        """Eliminates the first column in self.data"""
        newData = []
        for line in self.data:
            newData.append(line[1:])
        self.data = newData

    def seperateLabelsFromData(self) -> None:
        """Assigns y to be the first column of self.data and X to be the rest 
        of self.data"""
        self.y = []
        self.X = []
        for line in self.data:
            self.y.append(line[0])
            self.X.append(line[1:])
    
    def createXAndMockLabels(self) -> None:
        """Creates X and y so that if test data is passed in which doesn't have 
        labels, all of the other operations will still work"""
        self.X = self.data
        self.y = None

    def scaleValuesInX(self) -> None:
        """Scales the values in X that can be scaled"""
        self.scalePClass()
        self.binarySex()
        self.scaleAge()
        self.scaleSibSp()
        self.scaleParch()
        self.scaleFare()

    def elinateUneccessaryValuesInX(self) -> None:
        """Eliminates the values in X that are not useful"""
        self.eliminateName()
        self.eliminateTicketNumber()
        self.removeLastColumn()
        self.removeLastColumn()

    def scaleIndex(self, index:int, amount:float) -> None: 
        """Scales the values in a column in X specified by index by amount"""
        newX = []
        for passenger in self.X:
            passenger[index] *= amount
            newX.append(passenger)
        self.X = newX
    
    def scalePClass(self) -> None:
        """Scales the pClass column"""
        self.scaleIndex(0, 1.0/3.0)

    def binarySex(self) -> None:
        """Makes the sex column consist of 0's and 1's instead of strings"""
        newX = []
        sexIndex = 2
        for passenger in self.X:
            if(passenger[sexIndex] == "male"):
                passenger[sexIndex] = 1.0
            else:
                passenger[sexIndex] = 0.0
            newX.append(passenger)
        self.X = newX

    def scaleAge(self) -> None:
        """Scales the age column"""
        self.scaleIndex(3, 1.0/100.0)

    def scaleSibSp(self) -> None:
        """Scales the SibSp column"""
        self.scaleIndex(4, 1.0/8.0)

    def scaleParch(self) -> None:
        """Scales the Parch column"""
        self.scaleIndex(5, 1.0/6.0)

    def scaleFare(self) -> None:
        """Scales the Fare column"""
        self.scaleIndex(7, 1.0/512.0)

    def eliminateName(self) -> None:
        """Eliminates the name column from X"""
        newX = []
        for passenger in self.X:
            newPassenger = []
            newPassenger.append(passenger[0])
            otherNecessaryItems = passenger[2:]
            for otherNecessaryItem in otherNecessaryItems:
                newPassenger.append(otherNecessaryItem)
            newX.append(newPassenger)
        self.X = newX

    def eliminateTicketNumber(self) -> None:
        """Eliminates the Ticket number column from X"""
        newX = []
        for passenger in self.X:
            newPassenger = []
            firstItems = passenger[:5]
            lastItems = passenger[6:]
            for item in firstItems:
                newPassenger.append(item)
            for item in lastItems:
                newPassenger.append(item)
            newX.append(newPassenger)
            
        self.X = newX

    def removeLastColumn(self) -> None:
        """Eliminates the last column from X"""
        newX = []
        for passenger in self.X:
            newX.append(passenger[:-1])
        self.X = newX

    def replaceNans(self) -> None:
        """Replaces all nans in X with 0's"""
        for i in range(len(self.X)):
            for j in range(len(self.X[0])):
                if(np.isnan(self.X[i][j])):
                    self.X[i][j] = 0