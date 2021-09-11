import unittest

import tensorflow as tf
from utilities.savehistories.SaveAccAndValAccSeperateFiles import SaveAccAndValAccSeperateFiles

class SaveAccAndValAccSeperateFilesTest (unittest.TestCase):
    def setUp(self) -> None:
        self.saveAccAndValAccSeperateFiles = SaveAccAndValAccSeperateFiles()
        history1 = MockHistory([0.6, 0.7, 0.8], [0.6, 0.71, 0.79])
        history2 = MockHistory([0.2, 0.3, 0.6], [0.2, 0.3, 0.2])
        history3 = MockHistory([0.9, 0.9, 0.91], [0.6, 0.6, 0.64])
        self.saveAccAndValAccSeperateFiles.addHistory(history1, "hist1")
        self.saveAccAndValAccSeperateFiles.addHistory(history2, "hist2")
        self.saveAccAndValAccSeperateFiles.addHistory(history3, "hist3")

    def testCreateFilesWithLinesToSaveDict(self):
        self.saveAccAndValAccSeperateFiles._createFilesWithLinesToSaveDict()
        solution = {
            "AccuracyComparison" : [
                ["Epoch", "hist1", "hist2", "hist3"],
                [1, 0.6, 0.2, 0.9],
                [2, 0.7, 0.3, 0.9],
                [3 ,0.8, 0.6, 0.91]
            ],
            "ValAccuracyComparison" : [
                ["Epoch", "hist1", "hist2", "hist3"],
                [1, 0.6, 0.2, 0.6],
                [2, 0.71, 0.3, 0.6],
                [3 ,0.79, 0.2, 0.64]
            ]
        }
        self.assertEquals(self.saveAccAndValAccSeperateFiles._filesWithLinesToSave, solution)

class MockHistory (tf.keras.callbacks.History):
    """A mock keras history class to easily allow creation of history objects"""

    def __init__(self, acc, valAcc):
        super().__init__()
        self.history["accuracy"] = acc
        self.history["accuracy"] = valAcc