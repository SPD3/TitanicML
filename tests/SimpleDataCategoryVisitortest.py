from datacategoryvisitors.SimpleDataCategoryVisitor import SimpleDataCategoryVisitor
import unittest

class SimpleDataCategoryVisitorTest (unittest.TestCase):
    
    def test_visitPassengerId(self):
        simpleDataCategoryVisitor = SimpleDataCategoryVisitor()
        data = [1,2,3,4,5,6,7,8,9,10]
        solution = [[],[],[],[],[],[],[],[],[],[]]
        self.assertEquals(simpleDataCategoryVisitor.visitPassengerId(data), solution)
        