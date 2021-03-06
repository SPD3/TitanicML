from modelgenerators.ModelGeneratorBase import ModelGeneratorBase
from endtoenditerators.AllModelCombinationsIterator import AllModelCombinationsIterator
from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
import unittest
from datacategoryvisitors.CategorizedDataVisitor import CategorizedDataVisitor
from dataprocessors.DataProcessorWithVisitor import DataProcessorWithVisitor
from datacategoryvisitors.ScaledDataCategoryVisitor import ScaledDataCategoryVisitor
import numpy as np

class AllModelCombinationsIteratorTest (unittest.TestCase):
    """Test code for the AllModelCombinationsIterator class"""

    def setUp(self) -> None:
        """Sets up all of the model combinations"""
        data = [
            [1,0,3,"Braund, Mr. Owen Harris","male",22,1,0,"A/5 21171",7.25,np.nan,"S"],
            [2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)","female",38,1,0,"PC 17599",71.2833,"C85","C"],
            [3,1,3,"Heikkinen, Miss. Laina","female",26,0,0,"STON/O2. 3101282",7.925,np.nan,"S"]
        ]
        
        self._dataCategoryVisitors = [
            ScaledDataCategoryVisitor(),
            CategorizedDataVisitor()
        ]
        self._modelGenerators = [
            RectangularDenseModelGenerator("Test model"),
            RectangularDenseModelGenerator("Test model", 1024, 5),
            RectangularDenseModelGenerator("Test model", 2056, 3)
        ]
        self._dataProcessors = [
            DataProcessorWithVisitor(data, True),
        ]
        self._allModelCominationsIterator = AllModelCombinationsIterator(self._dataCategoryVisitors, self._dataProcessors, self._modelGenerators)

    def checkOutputTypes(self, output):
        """Makes sure that the output of the iterator is of the types expected"""
        X, y, modelGenerator, name = output
        self.assertEquals(type(X), np.ndarray)
        self.assertEquals(type(y), np.ndarray)
        self.assertEquals(type(modelGenerator), RectangularDenseModelGenerator)
        self.assertEquals(type(name), str)

    def testFirst(self):
        """Makes sure that the first item is of the type expected and resets 
        the iteration back to the first item"""
        
        output = self._allModelCominationsIterator._first()
        self.checkOutputTypes(output)
        currentItem = self._allModelCominationsIterator._currentItem()
        self.assertEquals(output[0].tolist(), currentItem[0].tolist())
        self.assertEquals(output[1].tolist(), currentItem[1].tolist())
        self.assertEquals(output[2], currentItem[2])
        self.assertEquals(output[3], currentItem[3])
        
    def testIsDone(self):
        """Makes sure isDone returns true """
        for i in range(6):
            self.assertFalse(self._allModelCominationsIterator._isDone())
            self._allModelCominationsIterator._next()
        self.assertTrue(self._allModelCominationsIterator._isDone())
        self._allModelCominationsIterator._first()

    def _makeSureOutputIsUnique(self, listOfOutputs:list[tuple[np.ndarray, np.ndarray, ModelGeneratorBase, str]], newOutput:tuple[np.ndarray, np.ndarray, ModelGeneratorBase, str]):
        """Makes sure that the new output is not the same as any of the previous
        outputs"""
        for output in listOfOutputs:
            outputX = output[1].tolist()
            outputY = output[0].tolist()
            outputModelGenerator = output[2]
            newOutputX = newOutput[1].tolist()
            newOutputY = newOutput[0].tolist()
            newOutputModelGenerator = newOutput[2]

            sameX = outputX == newOutputX
            sameY = outputY == newOutputY
            sameModelGenerator = outputModelGenerator == newOutputModelGenerator
            self.assertFalse(sameX and sameY and sameModelGenerator, msg="One of the new outputs was not unique relative to the previous outputs.")

            sameName = output[3] == newOutput[3]
            self.assertFalse(sameName, msg="The names of any two outputs should be unique")

    def testNextAndCurrentItem(self):
        """Tests the normal flow of the iterator"""
        self._allModelCominationsIterator._first()
        listOfOutputs = []
        numOfLoops = 0
        while(not self._allModelCominationsIterator._isDone()):
            currentOutput = self._allModelCominationsIterator._currentItem()
            self.checkOutputTypes(currentOutput)
            self._makeSureOutputIsUnique(listOfOutputs, currentOutput)
            listOfOutputs.append(currentOutput)
            self.assertLessEqual(numOfLoops, 10, msg="Too many loops!")
            
            self._allModelCominationsIterator._next()
            numOfLoops += 1
            
    def testPythonInterationLoops(self):
        """Tests the built in interation within python with the 
        AllModelCominationsIterator"""
        listOfOutputs = []
        numOfLoops = 0
        for currentOutput in self._allModelCominationsIterator:
            self.checkOutputTypes(currentOutput)
            self._makeSureOutputIsUnique(listOfOutputs, currentOutput)
            listOfOutputs.append(currentOutput)
            self.assertLessEqual(numOfLoops, 10, msg="Too many loops!")
            
            numOfLoops += 1

    def testGetName(self):
        """Tests the get name function within the iterator by getting the first 
        item and making sure that the name is correct"""
        self._allModelCominationsIterator._first()
        name = self._allModelCominationsIterator._getName()
        solution = str(self._dataCategoryVisitors[0]) + "_" + str(self._dataProcessors[0]) + "_" + str(self._modelGenerators[0])
        self.assertEquals(name, solution)


