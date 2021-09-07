from datacategoryvisitors.processeddatabuilders.NameClassifierBuilder import NameClassifierBuilder
import unittest

class NameClassifierBuilderTest (unittest.TestCase):
    """Tests the NameClassifierBuilder"""
    def setUp(self) -> None:
        self.nameClassifierBuilder = NameClassifierBuilder()

    def test_getTitle(self):
        """Makes sure that getTitle does find titles"""
        def checkNameAndTitle(name, titlesolution):
            title = self.nameClassifierBuilder._getTitle(name)
            self.assertEquals(titlesolution, title)

        checkNameAndTitle("Mrs. ldajfhgp", "Mrs")
        checkNameAndTitle("dlsfajkMrdlkjaf", "Mr")
        checkNameAndTitle("dagddgwdasJonkheer", "Jonkheer")

    def testInitializeNameMapping(self) -> None:
        """Makes sure that initializeNameMapping() creates a list 6 bins long 
        and is all 0s"""
        self.nameClassifierBuilder._initializeNameMapping()
        self.assertEquals(type(self.nameClassifierBuilder._currentNameMapping), list)
        solution = [0.0,0.0,0.0,0.0,0.0,0.0]
        self.assertEquals(solution, self.nameClassifierBuilder._currentNameMapping)

    def testMapTitle(self) -> None:
        """Makes sure that mapTitle() maps various titles to the correct bin"""
        def testNewTitle(name:str, solution:list[float]):
            self.nameClassifierBuilder._initializeNameMapping()
            title = self.nameClassifierBuilder._getTitle(name)
            self.nameClassifierBuilder._mapTitle(title)
            self.assertEquals(solution, self.nameClassifierBuilder._currentNameMapping)

        solution = [1.0,0.0,0.0,0.0,0.0,0.0]
        testNewTitle("jslghaldfaCollgja lgn awfggad", solution)
        
        solution = [0.0,0.0,1.0,0.0,0.0,0.0]
        testNewTitle("fsdj Mrs. afjdlgaj", solution)

        solution = [0.0,0.0,0.0,0.0,0.0,1.0]
        testNewTitle("jslghaldfagja lgn awfggad", solution)

    def testBuildProcessedData(self) -> None:
        """Makes sure that for every name passed in it's title is binned and 
        appended to processedData"""
        preprocessedData = ["jglskajgCaptgakljd", "MissMissMissMiss", "Don akgjdflagjkl", "aafdfdDr"]
        self.nameClassifierBuilder._preprocessedData = preprocessedData
        self.nameClassifierBuilder._buildProcessedData()
        solution = [
            [1.0,0.0,0.0,0.0,0.0,0.0],
            [0.0,1.0,0.0,0.0,0.0,0.0],
            [1.0,0.0,0.0,0.0,0.0,0.0],
            [0.0,0.0,0.0,1.0,0.0,0.0]
        ]
        self.assertEquals(solution, self.nameClassifierBuilder._processedData)
