from preprocessdata.PreProcessDataBase import PreProcessDataBase
import pandas as pd
import numpy as np

class SimpleDataPreProcessor (PreProcessDataBase):
    """First data attempt at processing data. This code is deprecated and 
    DataPreProcessorWithVisitor Should be used instead"""

    def __init__(self, data:np.ndarray, dataIncludesLabels:bool=True) -> None:
        super().__init__(data, dataIncludesLabels)
        self._dataIsProcessed = False

    def getProcessedData(self) -> tuple[np.ndarray, np.ndarray]:
        """Processed the data if it has not been yet and then returns y and X"""
        if(not self._dataIsProcessed):
            self.__processData()
        return np.array(self._y), np.array(self._X)

    def __processData(self) -> None:
        """Processes the data. Eliminates useless data, and relabels useful data
         in ways that a ML algorithm can use"""
        self.__eliminateFirstColumnInTrainData()
        if(self._dataIncludesLabels):
            self.__seperateLabelsFromData()
        else:
            self.__createXAndMockLabels()
        self.__scaleValuesInX()
        self.elinateUneccessaryValuesInX()
        self.replaceNans()
        self._dataIsProcessed = True

    def __eliminateFirstColumnInTrainData(self) -> None:
        """Eliminates the first column in self.data"""
        newData = []
        for line in self._data:
            newData.append(line[1:])
        self._data = newData

    def __seperateLabelsFromData(self) -> None:
        """Assigns y to be the first column of self.data and X to be the rest 
        of self.data"""
        self._y = []
        self._X = []
        for line in self._data:
            self._y.append(line[0])
            self._X.append(line[1:])
    
    def __createXAndMockLabels(self) -> None:
        """Creates X and y so that if test data is passed in which doesn't have 
        labels, all of the other operations will still work"""
        self._X = self._data
        self._y = None

    def __scaleValuesInX(self) -> None:
        """Scales the values in X that can be scaled"""
        self.__scalePClass()
        self.__binarySex()
        self.__scaleAge()
        self.__scaleSibSp()
        self.__scaleParch()
        self.__scaleFare()

    def elinateUneccessaryValuesInX(self) -> None:
        """Eliminates the values in X that are not useful"""
        self.__eliminateName()
        self.__eliminateTicketNumber()
        self.__removeLastColumn()
        self.__removeLastColumn()

    def __scaleIndex(self, index:int, amount:float) -> None: 
        """Scales the values in a column in X specified by index by amount"""
        newX = []
        for passenger in self._X:
            passenger[index] *= amount
            newX.append(passenger)
        self._X = newX
    
    def __scalePClass(self) -> None:
        """Scales the pClass column"""
        self.__scaleIndex(0, 1.0/3.0)

    def __binarySex(self) -> None:
        """Makes the sex column consist of 0's and 1's instead of strings"""
        newX = []
        sexIndex = 2
        for passenger in self._X:
            if(passenger[sexIndex] == "male"):
                passenger[sexIndex] = 1.0
            else:
                passenger[sexIndex] = 0.0
            newX.append(passenger)
        self._X = newX

    def __scaleAge(self) -> None:
        """Scales the age column"""
        self.__scaleIndex(3, 1.0/100.0)

    def __scaleSibSp(self) -> None:
        """Scales the SibSp column"""
        self.__scaleIndex(4, 1.0/8.0)

    def __scaleParch(self) -> None:
        """Scales the Parch column"""
        self.__scaleIndex(5, 1.0/6.0)

    def __scaleFare(self) -> None:
        """Scales the Fare column"""
        self.__scaleIndex(7, 1.0/512.0)

    def __eliminateName(self) -> None:
        """Eliminates the name column from X"""
        newX = []
        for passenger in self._X:
            newPassenger = []
            newPassenger.append(passenger[0])
            otherNecessaryItems = passenger[2:]
            for otherNecessaryItem in otherNecessaryItems:
                newPassenger.append(otherNecessaryItem)
            newX.append(newPassenger)
        self._X = newX

    def __eliminateTicketNumber(self) -> None:
        """Eliminates the Ticket number column from X"""
        newX = []
        for passenger in self._X:
            newPassenger = []
            firstItems = passenger[:5]
            lastItems = passenger[6:]
            for item in firstItems:
                newPassenger.append(item)
            for item in lastItems:
                newPassenger.append(item)
            newX.append(newPassenger)
            
        self._X = newX

    def __removeLastColumn(self) -> None:
        """Eliminates the last column from X"""
        newX = []
        for passenger in self._X:
            newX.append(passenger[:-1])
        self._X = newX

    def replaceNans(self) -> None:
        """Replaces all nans in X with 0's"""
        for i in range(len(self._X)):
            for j in range(len(self._X[0])):
                if(np.isnan(self._X[i][j])):
                    self._X[i][j] = 0