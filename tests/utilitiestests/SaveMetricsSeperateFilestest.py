import unittest

import tensorflow as tf
from utilities.savehistories.SaveMetricsSeperateFiles import SaveMetricsSeperateFiles

class SaveMetricsSeperateFilesTest (unittest.TestCase):
    """Test code for the SaveMetricsSeperateFiles class which makes sure 
    that accuracy and validation accuracy are saved in seperate files for a 
    given set of histories"""

    def setUp(self) -> None:
        metrics = [
            ("Acc_and_ValAcc", ["accuracy", "val_accuracy"]),
            ("Acc", ["accuracy"]),
            ("ValAcc", ["val_accuracy"])
        ]
        self.saveMetricsSeperateFiles = SaveMetricsSeperateFiles(metrics, "name")
        history1 = MockHistory([0.6, 0.7, 0.8], [0.6, 0.71, 0.79])
        history2 = MockHistory([0.2, 0.3, 0.6], [0.2, 0.3, 0.2])
        history3 = MockHistory([0.9, 0.9, 0.91], [0.6, 0.6, 0.64])
        self.saveMetricsSeperateFiles.addHistory(history1, "hist1")
        self.saveMetricsSeperateFiles.addHistory(history2, "hist2")
        self.saveMetricsSeperateFiles.addHistory(history3, "hist3")

    def testCreateFilesWithLinesToSaveDict(self):
        """Makes sure that _createFilesWithLinesToSaveDict creates lines 
        correctly for the data passed in so that a csv file can be created"""
        self.saveMetricsSeperateFiles._createFilesWithLinesToSaveDict()
        solution = {
            "nameAcc_and_ValAcc" : [
                ["Epoch", "hist1accuracy", "hist1val_accuracy", "hist2accuracy", "hist2val_accuracy", "hist3accuracy", "hist3val_accuracy",],
                [1, 0.6, 0.6, 0.2, 0.2, 0.9, 0.6],
                [2, 0.7, 0.71, 0.3, 0.3, 0.9, 0.6],
                [3 ,0.8, 0.79, 0.6, 0.2, 0.91, 0.64]
            ],
            "nameAcc" : [
                ["Epoch", "hist1accuracy", "hist2accuracy", "hist3accuracy"],
                [1, 0.6, 0.2, 0.9],
                [2, 0.7, 0.3, 0.9],
                [3 ,0.8, 0.6, 0.91]
            ],
            "nameValAcc" : [
                ["Epoch", "hist1val_accuracy", "hist2val_accuracy", "hist3val_accuracy"],
                [1, 0.6, 0.2, 0.6],
                [2, 0.71, 0.3, 0.6],
                [3, 0.79, 0.2, 0.64]
            ]
        }
        self.assertEquals(self.saveMetricsSeperateFiles._filesWithLinesToSave, solution)

    def testAddNameToFirstLine(self):
        """Tests the addNameToFirstLine method"""
        myList = [
            ["1", "2"],
            [1, 2],
            [1, 2],
            [1, 2],
        ]
        self.saveMetricsSeperateFiles._addNameToFirstLine("John", myList)
        solution = [
            ["1", "2", "John"],
            [1, 2],
            [1, 2],
            [1, 2],
        ]
        self.assertEquals(myList, solution)

    def testSetUpEpochLines(self):
        """Tests the _setUpEpochLines method to make sure that epoch numbers are
         added to _filesWithLinesToSave in the correct list format"""
        self.saveMetricsSeperateFiles._filesWithLinesToSave = {
            "AccuracyComparison": [
                ["Epoch"]
            ],
            "ValAccuracyComparison": [
                ["Epoch"]
            ],
        }
        self.saveMetricsSeperateFiles._setUpEpochLines()
        solution = {
            "AccuracyComparison": [
                ["Epoch"],
                [1],
                [2],
                [3]
            ],
            "ValAccuracyComparison": [
                ["Epoch"],
                [1],
                [2],
                [3]
            ],
        }
        self.assertEquals(self.saveMetricsSeperateFiles._filesWithLinesToSave, solution)

    def testAddMetricToLines(self):
        """Tests the _addMetricToLines method to makes sure that metric values 
        are added to their corresponding epochs"""
        metric = [1,2,3,4]
        lines = [
            [5],
            [6],
            [7],
            [8]
        ]
        self.saveMetricsSeperateFiles._addMetricToLines(metric, lines)
        solution = [
            [5,1],
            [6,2],
            [7,3],
            [8,4]
        ]
        self.assertEquals(lines, solution)

class MockHistory (tf.keras.callbacks.History):
    """A mock keras history class to easily allow creation of history objects"""

    def __init__(self, acc:list[float], valAcc:list[float]):
        super().__init__()
        self.history["accuracy"] = acc
        self.history["val_accuracy"] = valAcc
    