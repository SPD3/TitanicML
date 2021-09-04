from datacategoryvisitors.SimpleDataCategoryVisitor import SimpleDataCategoryVisitor
import unittest
from preprocessdata.DataPreProcessorWithVisitor import DataPreProcessorWithVisitor
import numpy as np

class DataPreProcessorWithVisitorTest (unittest.TestCase):

    def test_putDataIntoCategories(self):
        data = [
            [1,0,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,1,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        dataPreProcessorWithVisitor = DataPreProcessorWithVisitor(data, True, SimpleDataCategoryVisitor())
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
    
    def test_putDataIntoCategoriesWithoutSolutions(self):
        data = [
            [1,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        dataPreProcessorWithVisitor = DataPreProcessorWithVisitor(data, False, SimpleDataCategoryVisitor())
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

    def test_getProcessedData(self):
        data = [
            [1,0,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,1,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        
        dataPreProcessorWithVisitor = DataPreProcessorWithVisitor(data, True, SimpleDataCategoryVisitor())
        y, X = dataPreProcessorWithVisitor.getProcessedData()
        solutionY = [0,1,1]
        solutionX = [
            [1.0, 1.0, 22.0/100.0, 1.0/8.0, 0.0, 7.25/512.0],
            [1.0/3.0, 0.0, 38/100.0, 1.0/8.0, 0.0, 71.2833/512.0],
            [1.0, 0.0, 26/100.0, 0.0, 0.0, 7.925/512.0]
        ]
        self.assertEquals(solutionY, y.tolist())
        self.assertEquals(solutionX, X.tolist())