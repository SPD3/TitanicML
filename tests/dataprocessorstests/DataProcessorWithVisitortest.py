from datacategoryvisitors.CategorizedDataVisitor import CategorizedDataVisitor
from datacategoryvisitors.DataCategoryVisitorBase import DataCategoryVisitorBase
from datacategoryvisitors.ScaledDataCategoryVisitor import ScaledDataCategoryVisitor
import unittest
from dataprocessors.DataProcessorWithVisitor import DataProcessorWithVisitor
import numpy as np

class DataProcessorWithVisitorTest (unittest.TestCase):
    """Test for the DataProcessorWithVisitor class"""

    def testSetDataCategoryVisitor(self):
        data = [[]]
        dataProcessorWithVisitor = DataProcessorWithVisitor(data, True, ScaledDataCategoryVisitor())
        self.assertEquals(type(dataProcessorWithVisitor._dataCategoryVisitor), ScaledDataCategoryVisitor)
        dataProcessorWithVisitor.setDataCategoryVisitor(CategorizedDataVisitor())
        self.assertEquals(type(dataProcessorWithVisitor._dataCategoryVisitor), CategorizedDataVisitor)

    def testGetCategoryDictionary(self) -> None:
        """Makes sure that the category dictionary is generate with the
        correct keys"""
        data = [[]]
        dataProcessorWithVisitor = DataProcessorWithVisitor(data, True, ScaledDataCategoryVisitor())
        solution = ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age",
            "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]
        keys = dataProcessorWithVisitor.getCategoryDictionary().keys()
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
        
        dataProcessorWithVisitor = DataProcessorWithVisitor(data, True, ScaledDataCategoryVisitor())
        y, X = dataProcessorWithVisitor.getProcessedData()
        solutionY = [0,1,1]
        solutionX = [
            [1.0,   1.0,0.0,0.0,0.0,0.0,0.0,     1.0, 22.0/80.0, 1.0/8.0, 0.0,  0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,    7.25/512.0,    1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,    1.0,0.0,0.0],
            [1.0/3.0,   0.0,0.0,1.0,0.0,0.0,0.0,     0.0, 38/80.0, 1.0/8.0, 0.0,    0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,    71.2833/512.0, 0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,    0.0,1.0,0.0],
            [1.0,    0.0,1.0,0.0,0.0,0.0,0.0,    0.0, 26/80.0, 0.0, 0.0,   0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,     7.925/512.0, 1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,      1.0,0.0,0.0]
        ]
        
        self.assertEquals(type(y), np.ndarray, msg="Y needs to be a numpy array")
        self.assertEquals(type(X), np.ndarray, msg="X needs to be a numpy array")
        self.assertEquals(len(y.shape), 1, msg="Y needs to be a 1d array")
        self.assertEquals(len(X.shape), 2, msg="X needs to be a 2d array")
        length = len(X[0])
        for example in X:
            self.assertEquals(len(example), length, msg="The examples in X need to be all the same length")
        
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
        dataProcessorWithVisitor = DataProcessorWithVisitor(data, True, ScaledDataCategoryVisitor())
        dataProcessorWithVisitor._putDataIntoCategories()
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
        self.assertEquals(dataProcessorWithVisitor.getCategoryDictionary(), solution)
    
    def testPutDataIntoCategoriesWithoutLabels(self) -> None:
        """Tests to makes sure that the putDataIntoCategories() seperates the 
        out the columns of data into seperate categories in a dictionary when 
        labels are not passed in with the data"""
        data = [
            [1,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        dataProcessorWithVisitor = DataProcessorWithVisitor(data, False, ScaledDataCategoryVisitor())
        dataProcessorWithVisitor._putDataIntoCategories()
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
        categoryDictionary = dataProcessorWithVisitor.getCategoryDictionary()
        self.assertEquals(categoryDictionary, solution)

    def testVisitAllDataCategories(self):
        """Uses a dummy visitor to make sure that all categories are visited"""
        visitor = DummyVisitor()
        data = [
            [1,0,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,1,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        dataProcessorWithVisitor = DataProcessorWithVisitor(data, True, visitor)
        dataProcessorWithVisitor._visitAllDataCategories()
        self.assertTrue(visitor.visitedAllCategories())
    
    def testArrangeDataPerPassengerInXAndY(self):
        """Makes sure that _arrangeDataPerPassengerInXAndY() converts the 
        category dictionary into X and y lists"""
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

        dataProcessorWithVisitor = DataProcessorWithVisitor(data, True, None)
        dataProcessorWithVisitor._categoryDictionary = categoryDictionary
        dataProcessorWithVisitor._arrangeDataPerPassengerInXAndY()
        solutionX = [
            [1,3,"One", "male", 22, 1,0,"T1",5,np.nan,"S",2,3],
            [2,1,"Two", "female", 38, 1,0,"T2",50,"C85","C",4,5],
            [3,3,"Three", "female", 26, 0,0,"T3",300,np.nan,"S",7,8]
        ]
        solutionY = [1,0,1]
        dataProcessorWithVisitor._X
        self.assertEquals(solutionX, dataProcessorWithVisitor._X)
        self.assertEquals(solutionY, dataProcessorWithVisitor._y)

    def testString(self) -> None:
        """Tests the string representation of DataProcessorWithVisitor"""
        data = [1,2,3]

        dataProcessorWithVisitor = DataProcessorWithVisitor(data, True, None)
        self.assertEquals(str(dataProcessorWithVisitor), "ProcWithVis")

    def testResetData(self) -> None:
        """Tests to see if the member variables are reset correctly within 
        DataProcessorWithVisitor when reset is called so that subsequent 
        calls to getting the processed data will reprocess data"""
        visitor = ScaledDataCategoryVisitor()
        data = [
            [1,0,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,1,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        dataProcessorWithVisitor = DataProcessorWithVisitor(data, True, visitor)
        dataProcessorWithVisitor.getProcessedData()
        dataProcessorWithVisitor._resetData()
        self.assertFalse(dataProcessorWithVisitor._hasProcessedData)
        for list in dataProcessorWithVisitor.getCategoryDictionary().values():
            self.assertEquals(list, [])
        self.assertEquals(dataProcessorWithVisitor._X, [])
        self.assertEquals(dataProcessorWithVisitor._y, [])


class DummyVisitor (DataCategoryVisitorBase):
    """A dummy visitor class that just keeps track of which categories have been
     visited"""
    def __init__(self) -> None:
        self._categoryDictionary = {
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
        self._categoryDictionary["PassengerId"] = True
        return [[]]

    def visitSurvived(self, survived:list[int]) -> list[list[float]]:
        self._categoryDictionary["Survived"] = True
        return [[]]

    def visitPclass(self, pClass:list[int]) -> list[list[float]]:
        self._categoryDictionary["Pclass"] = True
        return [[]]

    def visitName(self, name:list[str]) -> list[list[float]]:
        self._categoryDictionary["Name"] = True
        return [[]]

    def visitSex(self, sex:list[str]) -> list[list[float]]:
        self._categoryDictionary["Sex"] = True
        return [[]]

    def visitAge(self, age:list[float]) -> list[list[float]]:
        self._categoryDictionary["Age"] = True
        return [[]]

    def visitSibSp(self, sibSp:list[int]) -> list[list[float]]:
        self._categoryDictionary["SibSp"] = True
        return [[]]

    def visitParch(self, parch:list[int]) -> list[list[float]]:
        self._categoryDictionary["Parch"] = True
        return [[]]

    def visitTicket(self, ticket:list) -> list[list[float]]:
        self._categoryDictionary["Ticket"] = True
        return [[]]

    def visitFare(self, fare:list[float]) -> list[list[float]]:
        self._categoryDictionary["Fare"] = True
        return [[]]

    def visitCabin(self, cabin:list) -> list[list[float]]:
        self._categoryDictionary["Cabin"] = True
        return [[]]

    def visitEmbarked(self, embarked:list[str]) -> list[list[float]]:
        self._categoryDictionary["Embarked"] = True
        return [[]]

    def visitedAllCategories(self) -> bool:
        for visitedCategory in self._categoryDictionary.values():
            if(not visitedCategory):
                return False
        return True