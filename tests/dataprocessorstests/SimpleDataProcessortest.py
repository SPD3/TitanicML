from dataprocessors.SimpleDataProcessor import SimpleDataProcessor
import unittest
import numpy as np
from dataprocessors.SimpleDataProcessor import SimpleDataProcessor

class SimpleDataProcessorTest (unittest.TestCase):
    """Tests for the SimpleDataProcessor class"""

    def test_eliminateFirstColumn(self):
        """Makes sure that eliminateFirstColumnInTrainData() elimates the first 
        column in data"""
        data = [[1,2,3], [4,5,6], [7,8,9]]
        simpleDataProcessor = SimpleDataProcessor(data)
        simpleDataProcessor._eliminateFirstColumnInTrainData()
        solution = [[2,3], [5,6], [8,9]]
        self.assertEqual(simpleDataProcessor._data, solution)

    def test_seperateLabelsFromData(self):
        """Makes sure that seperateLabelsFromData() seperates the first column 
        from the rest and assigns them to y and X respectively"""
        data = [[1,2,3], [4,5,6], [7,8,9]]
        simpleDataProcessor = SimpleDataProcessor(data)
        simpleDataProcessor._seperateLabelsFromData()
        solutionX = [[2,3], [5,6], [8,9]]
        solutionY = [1,4,7]
        self.assertEqual(simpleDataProcessor._X, solutionX)
        self.assertEqual(simpleDataProcessor._y, solutionY)

    def test_scaleIndex(self):
        """Make sure that scaleIndex() scales all the values in a column in data 
        by the specified amount"""
        data = [[1,2,3], [4,5,6], [7,8,9]]
        simpleDataProcessor = SimpleDataProcessor(data)
        simpleDataProcessor._X = data
        simpleDataProcessor._scaleIndex(2, 1.0/9.0)
        solution = [[1,2,1.0/3.0], [4,5,2.0/3.0], [7,8,1.0]]
        self.assertEqual(simpleDataProcessor._X, solution)

    def test_binarySex(self):
        """Makes sure that the strings corresponding to sex in data are 
        converted to numerical values in binarySex()"""
        data = [[1,2,"male"], [4,5,"female"], [7,8,"male"]]
        simpleDataProcessor = SimpleDataProcessor(data)
        simpleDataProcessor._X = data
        simpleDataProcessor._binarySex()
        solution = [[1,2,1.0], [4,5,0.0], [7,8,1.0]]
        self.assertEqual(simpleDataProcessor._X, solution)

    def test_eliminateName(self):
        """Makes sure that names aare elinated in eliminateName()"""
        data = [[1,"Rachael",3], [4,"Lily",6], [7,"John",9]]
        simpleDataProcessor = SimpleDataProcessor(data)
        simpleDataProcessor._X = data
        simpleDataProcessor._eliminateName()
        solution = [[1,3], [4,6], [7,9]]
        self.assertEqual(simpleDataProcessor._X, solution)

    def test_eliminateTicketNumber(self):
        """Makes sure that ticket Numbers are elinated in 
        eliminateTicketNumber()"""
        data = [
            [1,2,3,4,5,"Ticket1",6,7,8], 
            [1.1,2.2,3.3,4.2,5.7,"Ticket2",6.6,7.4,8.1], 
            [1.9,2.5,3.7,4.6,5.3,"Ticket3",6.2,7.4,8.3]
        ]
        simpleDataProcessor = SimpleDataProcessor(data)
        simpleDataProcessor._X = data
        simpleDataProcessor._eliminateTicketNumber()
        solution = [    
            [1,2,3,4,5,6,7,8], 
            [1.1,2.2,3.3,4.2,5.7,6.6,7.4,8.1], 
            [1.9,2.5,3.7,4.6,5.3,6.2,7.4,8.3]
        ]
        self.assertEqual(simpleDataProcessor._X, solution)

    def test_removeLastColumn(self):
        """Makes sure that removeLastColumn() removes the last column in data"""
        data = [[1,2,3], [4,5,6], [7,8,9]]
        simpleDataProcessor = SimpleDataProcessor(data)
        simpleDataProcessor._X = data
        simpleDataProcessor._removeLastColumn()
        solution = [[1,2], [4,5], [7,8]]
        self.assertEqual(simpleDataProcessor._X, solution)

    def test_replaceNans(self):
        """Makes sure that replaceNans() will replace all nans in data with 
        0.0"""
        data = [[1,np.nan,3], [np.nan,5,6], [7,8,np.nan]]
        simpleDataProcessor = SimpleDataProcessor(data)
        simpleDataProcessor._X = data
        simpleDataProcessor.replaceNans()
        solution = [[1,0.0,3], [0.0,5,6], [7,8,0.0]]
        self.assertEqual(simpleDataProcessor._X, solution)

    def test_gettingRidOfLabels(self):
        """Makes sure that labels are taken out of X when getProcessedData() is 
        called"""
        data = [
            [1,2,3,4,5,6,7,8,9,10,11,12], 
            [4,5,6,7,8,9,0,1,2,13,14,15], 
            [7,8,9,0,1,2,3,4,5,16,17,18]
        ]
        simpleDataProcessor = SimpleDataProcessor(data)
        simpleDataProcessor.getProcessedData()
        self.assertEqual(len(simpleDataProcessor._X[0]), 6) 

    def test_notGettingRidOfLabels(self):
        """Makes sure that labels are not taken out of X when getProcessedData()
        is called and a boolean is passed in specifying that labels are not 
        included in data"""
        data = [
            [2,3,4,5,6,7,8,9,10,11,12], 
            [5,6,7,8,9,0,1,2,13,14,15], 
            [8,9,0,1,2,3,4,5,16,17,18]
        ]
        simpleDataProcessor = SimpleDataProcessor(data, dataIncludesLabels=False)
        simpleDataProcessor.getProcessedData()
        self.assertEqual(len(simpleDataProcessor._X[0]), 6) 
    
    def test_askForDataTwice(self):
        """Makes sure that data does not get processed twice."""
        data = [
            [1,2,3,4,5,6,7,8,9,10,11,12], 
            [4,5,6,7,8,9,0,1,2,13,14,15], 
            [7,8,9,0,1,2,3,4,5,16,17,18]
        ]
        simpleDataProcessor = SimpleDataProcessor(data)
        simpleDataProcessor.getProcessedData()
        simpleDataProcessor.getProcessedData()
        self.assertEqual(len(simpleDataProcessor._X[0]), 6)
