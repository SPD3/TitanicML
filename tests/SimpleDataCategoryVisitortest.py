from datacategoryvisitors.ScaledDataCategoryVisitor import ScaledDataCategoryVisitor
import unittest

class ScaledDataCategoryVisitorTest (unittest.TestCase):
    """Tests the ScaledDataCategoryVisitor class"""
    
    def test_visitPassengerId(self):
        """Makes sure that passengerIds are destroyed in the 
        ScaledDataCategoryVisitor because they are useless information"""
        scaledDataCategoryVisitor = ScaledDataCategoryVisitor()
        data = [1,2,3,4,5,6,7,8,9,10]
        solution = [[],[],[],[],[],[],[],[],[],[]]
        self.assertEquals(scaledDataCategoryVisitor.visitPassengerId(data), solution)
        