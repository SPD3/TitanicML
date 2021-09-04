from preprocessdata.PreProcessDataBase import PreProcessDataBase
import pandas as pd
import numpy as np

class SimpleDataPreProcessor (PreProcessDataBase):

    def __init__(self, data, dataIncludesLabels=True) -> None:
        super().__init__(data, dataIncludesLabels)
        self.dataIsProcessed = False

    def getProcessedData(self):
        if(not self.dataIsProcessed):
            self.preProcessData()
        return np.array(self.y), np.array(self.X)

    def preProcessData(self):
        self.eliminateFirstColumnInTrainData()
        if(self.dataIncludesLabels):
            self.seperateLabelsFromData()
        else:
            self.createXAndMockLabels()
        self.scaleValuesInX()
        self.elinateUneccessaryValuesInX()
        self.replaceNans()
        self.dataIsProcessed = True

    def eliminateFirstColumnInTrainData(self):
        newData = []
        for line in self.data:
            newData.append(line[1:])
        self.data = newData

    def seperateLabelsFromData(self):
        self.y = []
        self.X = []
        for line in self.data:
            self.y.append(line[0])
            self.X.append(line[1:])
    
    def createXAndMockLabels(self):
        self.X = self.data
        self.y = None

    def scaleValuesInX(self):
        print("IN THE WRONG ONE!!!!")
        self.scalePClass()
        self.binarySex()
        self.scaleAge()
        self.scaleSibSp()
        self.scaleParch()
        self.scaleFare()

    def elinateUneccessaryValuesInX(self):
        self.eliminateName()
        self.eliminateTicketNumber()
        self.removeLastColumn()
        self.removeLastColumn()

    def scaleIndex(self, index, amount): 
        newX = []
        for passenger in self.X:
            passenger[index] *= amount
            newX.append(passenger)
        self.X = newX
    
    def scalePClass(self):
        self.scaleIndex(0, 1.0/3.0)

    def binarySex(self):
        newX = []
        sexIndex = 2
        for passenger in self.X:
            if(passenger[sexIndex] == "male"):
                passenger[sexIndex] = 1.0
            else:
                passenger[sexIndex] = 0.0
            newX.append(passenger)
        self.X = newX

    def scaleAge(self):
        self.scaleIndex(3, 1.0/100.0)

    def scaleSibSp(self):
        self.scaleIndex(4, 1.0/8.0)

    def scaleParch(self):
        self.scaleIndex(5, 1.0/6.0)

    def scaleFare(self):
        self.scaleIndex(7, 1.0/512.0)

    def eliminateName(self):
        newX = []
        for passenger in self.X:
            newPassenger = []
            newPassenger.append(passenger[0])
            otherNecessaryItems = passenger[2:]
            for otherNecessaryItem in otherNecessaryItems:
                newPassenger.append(otherNecessaryItem)
            newX.append(newPassenger)
        self.X = newX

    def eliminateTicketNumber(self):
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

    def removeLastColumn(self):
        newX = []
        for passenger in self.X:
            newX.append(passenger[:-1])
        self.X = newX

    def replaceNans(self):
        for i in range(len(self.X)):
            for j in range(len(self.X[0])):
                if(np.isnan(self.X[i][j])):
                    self.X[i][j] = 0