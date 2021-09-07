import unittest
from datacategoryvisitors.processeddatabuilders.CabinClassifierBuilder import CabinClassifierBuilder

class CabinClassifierBuilderTest (unittest.TestCase):

    def setUp(self) -> None:
        self._cabinClassifierBuilder = CabinClassifierBuilder()
    
    def testInitializeCabinMapping(self) -> None:
        """Makes sure that initializeCabinMapping() creates a list 9 bins long 
        and is all 0s"""
        self._cabinClassifierBuilder._initializeCabinMapping()
        self.assertEquals(type(self._cabinClassifierBuilder._currentCabinMapping), list)
        solution = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        self.assertEquals(solution, self._cabinClassifierBuilder._currentCabinMapping)

    def testMapCabin(self) -> None:
        """Makes sure that mapCabin() maps various ages to the correct bin"""
        def testNewCabinValue(cabin, solution:list[float]):
            self._cabinClassifierBuilder._initializeCabinMapping()
            self._cabinClassifierBuilder._mapCabin(cabin)
            self.assertEquals(solution, self._cabinClassifierBuilder._currentCabinMapping)

        solution = [0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0]
        testNewCabinValue("C85", solution)

        solution = [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        testNewCabinValue("A6", solution)

        solution = [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        testNewCabinValue(11, solution)

        solution = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0]
        testNewCabinValue("Z342", solution)

    def testBuildProcessedData(self) -> None:
        """Makes sure that for every cabin passed in it is binned and appended to 
        processedData"""

        preprocessedData = ["D47", "T1001", 3145, "X43"]
        self._cabinClassifierBuilder._preprocessedData = preprocessedData
        self._cabinClassifierBuilder._buildProcessedData()
        solution = [
            [0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],
            [0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0],
            [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
            [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0]
        ]
        self.assertEquals(solution, self._cabinClassifierBuilder._processedData)
