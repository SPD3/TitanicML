import numpy as np
from datacategoryvisitors.ScaledDataCategoryVisitor import ScaledDataCategoryVisitor
import unittest

class ScaledDataCategoryVisitorTest (unittest.TestCase):
    """Tests the ScaledDataCategoryVisitor class"""
    def setUp(self) -> None:
        self._scaledDataCategoryVisitor = ScaledDataCategoryVisitor()
    
    def testVisitPassengerId(self):
        """Makes sure that passengerIds are destroyed in the 
        ScaledDataCategoryVisitor because they are useless information"""
        data = [1,2,3,4,5,6,7,8,9,10]
        solution = [[],[],[],[],[],[],[],[],[],[]]
        passengers = self._scaledDataCategoryVisitor.visitPassengerId(data)
        self.assertEquals(solution, passengers)
    
    def testVisitSurvived(self) -> None:
        """Makes sure that visitSurvived() does nothing to the survived data"""
        data = [1, 0, 1, 1]
        passengers = self._scaledDataCategoryVisitor.visitSurvived(data)
        solution = [[1],[0],[1],[1]]
        self.assertEquals(solution, passengers)

    def _checkOneHotEncodingOfPassengers(self, passengers:list[list[int]]):
        """Checks that each passenger's encoding is the same length and that 
        each encoding is a one hot vector"""
        length = len(passengers[0])
        for passenger in passengers:
            msg = "The lengths of each passenger's encodings are not equal!"
            self.assertEquals(len(passenger), length, msg=msg)
            seenOne = False
            for value in passenger:
                if value == 0.0:
                    continue
                elif value == 1.0:
                    if seenOne:
                        msg = "multiple one's in this passenger: " + str(passenger)
                        self.fail(msg=msg)
                    seenOne = 1.0
                else:
                    msg = "A value other than 1 or 0 in passenger: " + str(passenger)
                    self.fail(msg=msg)

    def checkScaledEncodingOfPassengers(self, passengers:list[list[float]]):
        """Checks that each passenger's encoding is a list one value long and 
        that value is between 0 and 1"""
        length = 1
        for passenger in passengers:
            msg = "The lengths of each passenger's encoding should be 1!"
            self.assertEquals(len(passenger), length, msg=msg)

            value = passenger[0]
            self.assertLessEqual(value, 1.0)
            self.assertGreaterEqual(value, 0.0)

    def testVisitPclass(self) -> None:
        """Makes sure that visitPclass() scales its data"""
        data = [1, 3, 2, 1]
        passengers = self._scaledDataCategoryVisitor.visitPclass(data)
        self.assertEquals(len(data), len(passengers))
        self.checkScaledEncodingOfPassengers(passengers)

    def testVisitName(self) -> None:
        """Makes sure that visitName() bins its data in one hot vectors"""
        data = ["Mr. Jack", "Jackie Miss", "John Col James", "Nothing"]
        passengers = self._scaledDataCategoryVisitor.visitName(data)
        self.assertEquals(len(data), len(passengers))
        self._checkOneHotEncodingOfPassengers(passengers)

    def testVisitSex(self)  -> None:
        """Makes sure that visitSex() bins its data in one hot vectors"""
        data = ["female", "female", "female", "male"]
        passengers = self._scaledDataCategoryVisitor.visitSex(data)
        self.assertEquals(len(data), len(passengers))
        self._checkOneHotEncodingOfPassengers(passengers)

    def testVisitAge(self)  -> None:
        """Makes sure that visitAge() scales its data"""
        data = [0.55, 12, 78, 22]
        passengers = self._scaledDataCategoryVisitor.visitAge(data)
        self.assertEquals(len(data), len(passengers))
        self.checkScaledEncodingOfPassengers(passengers)

    def testVisitSibSp(self)  -> None:
        """Makes sure that visitSibSp() scales its data"""
        data = [5, 0, 3, 2]
        passengers = self._scaledDataCategoryVisitor.visitSibSp(data)
        self.assertEquals(len(data), len(passengers))
        self.checkScaledEncodingOfPassengers(passengers)

    def testVisitParch(self)  -> None:
        """Makes sure that visitParch() scales its data"""
        data = [4, 1, 0, 6]
        passengers = self._scaledDataCategoryVisitor.visitParch(data)
        self.assertEquals(len(data), len(passengers))
        self.checkScaledEncodingOfPassengers(passengers)

    def testVisitTicket(self)  -> None:
        """Makes sure that visitTicket() bins its data in one hot vectors"""
        data = [300000, "PP 4348", "A/5 21173", 151003]
        passengers = self._scaledDataCategoryVisitor.visitTicket(data)
        self.assertEquals(len(data), len(passengers))
        self._checkOneHotEncodingOfPassengers(passengers)

    def testVisitFare(self)  -> None:
        """Makes sure that visitFare() scales its data"""
        data = [22.5,  35, 7, 400]
        passengers = self._scaledDataCategoryVisitor.visitFare(data)
        self.assertEquals(len(data), len(passengers))
        self.checkScaledEncodingOfPassengers(passengers)

    def testVisitCabin(self)  -> None:
        """Makes sure that visitCabin() bins its data in one hot vectors"""
        data = ["D36",  "C78", np.nan, "B57 B59 B63 B66"]
        passengers = self._scaledDataCategoryVisitor.visitCabin(data)
        self.assertEquals(len(data), len(passengers))
        self._checkOneHotEncodingOfPassengers(passengers)

    def testVisitEmbarked(self)  -> None:
        """Makes sure that visitEmbarked() bins its data in one hot vectors"""
        data = ["Q",  "Q", "C", "S"]
        passengers = self._scaledDataCategoryVisitor.visitEmbarked(data)
        self.assertEquals(len(data), len(passengers))
        self._checkOneHotEncodingOfPassengers(passengers)
    
    def testString(self) -> None:
        """Tests the string representation of ScaledDataCategoryVisitor"""
        self.assertEquals(str(self._scaledDataCategoryVisitor), "ScalVis")