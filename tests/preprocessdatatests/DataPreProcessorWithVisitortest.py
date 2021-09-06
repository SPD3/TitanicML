from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase
from datacategoryvisitors.ScaledDataCategoryVisitor import ScaledDataCategoryVisitor
import unittest
from preprocessdata.DataPreProcessorWithVisitor import DataPreProcessorWithVisitor
import numpy as np

class DataPreProcessorWithVisitorTest (unittest.TestCase):
    """Test for the DataPreProcessorWithVisitor class"""

    def testGetCategoryDictionary(self) -> None:
        """Makes sure that the category dictionary is generate with the
        correct keys"""
        data = [[]]
        dataPreProcessorWithVisitor = DataPreProcessorWithVisitor(data, True, ScaledDataCategoryVisitor())
        solution = ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age",
            "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]
        keys = dataPreProcessorWithVisitor.getCategoryDictionary().keys()
        self.assertEquals(len(keys), len(solution))
        index = 0
        for key in keys:
            self.assertEquals(key, solution[index])
            index = index + 1


    def testGetProcessedData(self) -> None:
        """Makes sure that the data is processed before it is returned by 
        getProcessedData()"""
        data = [
            [1,0,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,1,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        
        dataPreProcessorWithVisitor = DataPreProcessorWithVisitor(data, True, ScaledDataCategoryVisitor())
        y, X = dataPreProcessorWithVisitor.getProcessedData()
        solutionY = [0,1,1]
        solutionX = [
            [1.0,   1.0,0.0,0.0,0.0,0.0,0.0,     1.0, 22.0/80.0, 1.0/8.0, 0.0,  0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,    7.25/512.0,    1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,    1.0,0.0,0.0],
            [1.0/3.0,   0.0,0.0,1.0,0.0,0.0,0.0,     0.0, 38/80.0, 1.0/8.0, 0.0,    0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,    71.2833/512.0, 0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,    0.0,1.0,0.0],
            [1.0,    0.0,1.0,0.0,0.0,0.0,0.0,    0.0, 26/80.0, 0.0, 0.0,   0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,     7.925/512.0, 1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,      1.0,0.0,0.0]
        ]
        for i in range(len(solutionX)):
            for j in range(len(solutionX[i])):
                self.assertAlmostEquals(X[i,j], solutionX[i][j], delta=0.001)
        self.assertEquals(solutionY, y.tolist())

    def testPutDataIntoCategories(self) -> None:
        """Tests to makes sure that the putDataIntoCategories() seperates the 
        out the columns of data into seperate categories in a dictionary"""
        data = [
            [1,0,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,1,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        dataPreProcessorWithVisitor = DataPreProcessorWithVisitor(data, True, ScaledDataCategoryVisitor())
        dataPreProcessorWithVisitor.putDataIntoCategories()
        solution = {
            "PassengerId" : [1,2,3],
            "Survived" : [0,1,1],
            "Pclass" : [3,1,3],
            "Name" : ["Braund, Mr. Owen Harris", "Cumings, Mrs. John Bradley (Florence Briggs Thayer)", "Heikkinen, Miss. Laina"],
            "Sex" : ["male", "female", "female"],
            "Age" : [22, 38, 26],
            "SibSp" : [1, 1, 0],
            "Parch" : [0, 0, 0],
            "Ticket" : ["A/5 21171",  "PC 17599", "STON/O2. 3101282"],
            "Fare" : [7.25, 71.2833, 7.925],
            "Cabin" : [np.nan, "C85", np.nan],
            "Embarked" : ["S", "C", "S"],
        }
        self.assertEquals(dataPreProcessorWithVisitor.getCategoryDictionary(), solution)
    
    def testPutDataIntoCategoriesWithoutLabels(self) -> None:
        """Tests to makes sure that the putDataIntoCategories() seperates the 
        out the columns of data into seperate categories in a dictionary when 
        labels are not passed in with the data"""
        data = [
            [1,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        dataPreProcessorWithVisitor = DataPreProcessorWithVisitor(data, False, ScaledDataCategoryVisitor())
        dataPreProcessorWithVisitor.putDataIntoCategories()
        solution = {
            "PassengerId" : [1,2,3],
            "Survived" : [],
            "Pclass" : [3,1,3],
            "Name" : ["Braund, Mr. Owen Harris", "Cumings, Mrs. John Bradley (Florence Briggs Thayer)", "Heikkinen, Miss. Laina"],
            "Sex" : ["male", "female", "female"],
            "Age" : [22, 38, 26],
            "SibSp" : [1, 1, 0],
            "Parch" : [0, 0, 0],
            "Ticket" : ["A/5 21171",  "PC 17599", "STON/O2. 3101282"],
            "Fare" : [7.25, 71.2833, 7.925],
            "Cabin" : [np.nan, "C85", np.nan],
            "Embarked" : ["S", "C", "S"],
        }
        categoryDictionary = dataPreProcessorWithVisitor.getCategoryDictionary()
        self.assertEquals(categoryDictionary, solution)

    def testVisitAllDataCategories(self):
        """Uses a dummy visitor to make sure that all categories are visited"""
        visitor = DummyVisitor()
        data = [
            [1,0,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,1,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        dataPreProcessorWithVisitor = DataPreProcessorWithVisitor(data, True, visitor)
        dataPreProcessorWithVisitor.visitAllDataCategories()
        self.assertTrue(visitor.visitedAllCategories())
    
    def testArrangeDataPerPassengerInXAndY(self):
        categoryDictionary = {
            "PassengerId" : [[1],[2],[3]],
            "Survived" : [[1],[0],[1]],
            "Pclass" : [[3],[1],[3]],
            "Name" : [["One"], ["Two"], ["Three"]],
            "Sex" : [["male"], ["female"], ["female"]],
            "Age" : [[22], [38], [26]],
            "SibSp" : [[1], [1], [0]],
            "Parch" : [[0], [0], [0]],
            "Ticket" : [["T1"],  ["T2"], ["T3"]],
            "Fare" : [[5], [50], [300]],
            "Cabin" : [[np.nan], ["C85"], [np.nan]],
            "Embarked" : [["S",2,3], ["C",4,5], ["S",7,8]],
        }
        data = [1,2,3]

        dataPreProcessorWithVisitor = DataPreProcessorWithVisitor(data, True, None)
        dataPreProcessorWithVisitor.categoryDictionary = categoryDictionary
        dataPreProcessorWithVisitor.arrangeDataPerPassengerInXAndY()
        solutionX = [
            [1,3,"One", "male", 22, 1,0,"T1",5,np.nan,"S",2,3],
            [2,1,"Two", "female", 38, 1,0,"T2",50,"C85","C",4,5],
            [3,3,"Three", "female", 26, 0,0,"T3",300,np.nan,"S",7,8]
        ]
        solutionY = [1,0,1]
        dataPreProcessorWithVisitor.X
        self.assertEquals(solutionX, dataPreProcessorWithVisitor.X)
        self.assertEquals(solutionY, dataPreProcessorWithVisitor.y)

class DummyVisitor (DataCategoryVisitorBase):
    def __init__(self) -> None:
        self.categoryDictionary = {
            "PassengerId" : False,
            "Survived" : False,
            "Pclass" : False,
            "Name" : False,
            "Sex" : False,
            "Age" : False,
            "SibSp" : False,
            "Parch" : False,
            "Ticket" : False,
            "Fare" : False,
            "Cabin" : False,
            "Embarked" : False,
        }

    def visitPassengerId(self, passengerId:list[int]) -> list[list[float]]:
        self.categoryDictionary["PassengerId"] = True
        return [[]]

    def visitSurvived(self, survived:list[int]) -> list[list[float]]:
        self.categoryDictionary["Survived"] = True
        return [[]]

    def visitPclass(self, pClass:list[int]) -> list[list[float]]:
        self.categoryDictionary["Pclass"] = True
        return [[]]

    def visitName(self, name:list[str]) -> list[list[float]]:
        self.categoryDictionary["Name"] = True
        return [[]]

    def visitSex(self, sex:list[str]) -> list[list[float]]:
        self.categoryDictionary["Sex"] = True
        return [[]]

    def visitAge(self, age:list[float]) -> list[list[float]]:
        self.categoryDictionary["Age"] = True
        return [[]]

    def visitSibSp(self, sibSp:list[int]) -> list[list[float]]:
        self.categoryDictionary["SibSp"] = True
        return [[]]

    def visitParch(self, parch:list[int]) -> list[list[float]]:
        self.categoryDictionary["Parch"] = True
        return [[]]

    def visitTicket(self, ticket:list) -> list[list[float]]:
        self.categoryDictionary["Ticket"] = True
        return [[]]

    def visitFare(self, fare:list[float]) -> list[list[float]]:
        self.categoryDictionary["Fare"] = True
        return [[]]

    def visitCabin(self, cabin:list) -> list[list[float]]:
        self.categoryDictionary["Cabin"] = True
        return [[]]

    def visitEmbarked(self, embarked:list[str]) -> list[list[float]]:
        self.categoryDictionary["Embarked"] = True
        return [[]]

    def visitedAllCategories(self) -> bool:
        for visitedCategory in self.categoryDictionary.values():
            if(not visitedCategory):
                return False
        return True