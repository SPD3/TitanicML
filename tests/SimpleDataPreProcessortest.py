import unittest
from preprocessdata.SimpleDataPreProcessor import SimpleDataPreProcessor
import numpy as np

class SimpleDataPreProcessorTest (unittest.TestCase):

    def test_eliminateFirstColumn(self):
        data = [[1,2,3], [4,5,6], [7,8,9]]
        simpleDataPreProcessor = SimpleDataPreProcessor(data)
        simpleDataPreProcessor.eliminateFirstColumnInTrainData()
        solution = [[2,3], [5,6], [8,9]]
        self.assertEqual(simpleDataPreProcessor.data, solution)

    def test_seperateLabelsFromData(self):
        data = [[1,2,3], [4,5,6], [7,8,9]]
        simpleDataPreProcessor = SimpleDataPreProcessor(data)
        simpleDataPreProcessor.seperateLabelsFromData()
        solutionX = [[2,3], [5,6], [8,9]]
        solutionY = [1,4,7]
        self.assertEqual(simpleDataPreProcessor.X, solutionX)
        self.assertEqual(simpleDataPreProcessor.y, solutionY)

    def test_scaleIndex(self):
        data = [[1,2,3], [4,5,6], [7,8,9]]
        simpleDataPreProcessor = SimpleDataPreProcessor(data)
        simpleDataPreProcessor.X = data
        simpleDataPreProcessor.scaleIndex(2, 1.0/9.0)
        solution = [[1,2,1.0/3.0], [4,5,2.0/3.0], [7,8,1.0]]
        self.assertEqual(simpleDataPreProcessor.X, solution)

    def test_binarySex(self):
        data = [[1,2,"male"], [4,5,"female"], [7,8,"male"]]
        simpleDataPreProcessor = SimpleDataPreProcessor(data)
        simpleDataPreProcessor.X = data
        simpleDataPreProcessor.binarySex()
        solution = [[1,2,1.0], [4,5,0.0], [7,8,1.0]]
        self.assertEqual(simpleDataPreProcessor.X, solution)

    def test_eliminateName(self):
        data = [[1,"Rachael",3], [4,"Lily",6], [7,"John",9]]
        simpleDataPreProcessor = SimpleDataPreProcessor(data)
        simpleDataPreProcessor.X = data
        simpleDataPreProcessor.eliminateName()
        solution = [[1,3], [4,6], [7,9]]
        self.assertEqual(simpleDataPreProcessor.X, solution)

    def test_eliminateTicketNumber(self):
        data = [
            [1,2,3,4,5,"Ticket1",6,7,8], 
            [1.1,2.2,3.3,4.2,5.7,"Ticket2",6.6,7.4,8.1], 
            [1.9,2.5,3.7,4.6,5.3,"Ticket3",6.2,7.4,8.3]
        ]
        simpleDataPreProcessor = SimpleDataPreProcessor(data)
        simpleDataPreProcessor.X = data
        simpleDataPreProcessor.eliminateTicketNumber()
        solution = [    
            [1,2,3,4,5,6,7,8], 
            [1.1,2.2,3.3,4.2,5.7,6.6,7.4,8.1], 
            [1.9,2.5,3.7,4.6,5.3,6.2,7.4,8.3]
        ]
        self.assertEqual(simpleDataPreProcessor.X, solution)

    def test_removeLastColumn(self):
        data = [[1,2,3], [4,5,6], [7,8,9]]
        simpleDataPreProcessor = SimpleDataPreProcessor(data)
        simpleDataPreProcessor.X = data
        simpleDataPreProcessor.removeLastColumn()
        solution = [[1,2], [4,5], [7,8]]
        self.assertEqual(simpleDataPreProcessor.X, solution)

    def test_replaceNans(self):
        data = [[1,np.nan,3], [np.nan,5,6], [7,8,np.nan]]
        simpleDataPreProcessor = SimpleDataPreProcessor(data)
        simpleDataPreProcessor.X = data
        simpleDataPreProcessor.replaceNans()
        solution = [[1,0.0,3], [0.0,5,6], [7,8,0.0]]
        self.assertEqual(simpleDataPreProcessor.X, solution)

    def test_gettingRidOfLabels(self):
        data = [
            [1,2,3,4,5,6,7,8,9,10,11,12], 
            [4,5,6,7,8,9,0,1,2,13,14,15], 
            [7,8,9,0,1,2,3,4,5,16,17,18]
        ]
        simpleDataPreProcessor = SimpleDataPreProcessor(data)
        simpleDataPreProcessor.getProcessedData()
        self.assertEqual(len(simpleDataPreProcessor.X[0]), 6) 

    def test_notGettingRidOfLabels(self):
        data = [
            [2,3,4,5,6,7,8,9,10,11,12], 
            [5,6,7,8,9,0,1,2,13,14,15], 
            [8,9,0,1,2,3,4,5,16,17,18]
        ]
        simpleDataPreProcessor = SimpleDataPreProcessor(data, dataIncludesLabels=False)
        simpleDataPreProcessor.getProcessedData()
        self.assertEqual(len(simpleDataPreProcessor.X[0]), 6) 
    
    def test_askForDataTwice(self):
        data = [
            [1,2,3,4,5,6,7,8,9,10,11,12], 
            [4,5,6,7,8,9,0,1,2,13,14,15], 
            [7,8,9,0,1,2,3,4,5,16,17,18]
        ]
        simpleDataPreProcessor = SimpleDataPreProcessor(data)
        simpleDataPreProcessor.getProcessedData()
        simpleDataPreProcessor.getProcessedData()
        self.assertEqual(len(simpleDataPreProcessor.X[0]), 6)
