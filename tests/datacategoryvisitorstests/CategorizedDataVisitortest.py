from datacategoryvisitors.CategorizedDataVisitor import CategorizedDataVisitor
import unittest
import numpy as np

class CategorizedDataVisitorTest (unittest.TestCase):
    """Tests the CategorizedDataVisitor class"""
    def setUp(self) -> None:
        self.categorizedDataVisitor = CategorizedDataVisitor()

    def testVisitPassengerId(self) -> None:
        """Makes sure that visitPassengerId() destroys the passenger ID data"""
        data = [10, 55, 22, 84]
        passengers = self.categorizedDataVisitor.visitPassengerId(data)
        solution = [[],[],[],[]]
        self.assertEquals(solution, passengers)
    
    def testVisitSurvived(self) -> None:
        """Makes sure that visitSurvived() does nothing to the survived data"""
        data = [1, 0, 1, 1]
        passengers = self.categorizedDataVisitor.visitSurvived(data)
        solution = [[1],[0],[1],[1]]
        self.assertEquals(solution, passengers)

    def checkOneHotEncodingOfPassengers(self, passengers:list[list[int]]):
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


    def testVisitPclass(self) -> None:
        """Makes sure that visitPclass() bins its data in one hot vectors"""
        data = [1, 3, 2, 1]
        passengers = self.categorizedDataVisitor.visitPclass(data)
        self.assertEquals(len(data), len(passengers))
        self.checkOneHotEncodingOfPassengers(passengers)

    def testVisitName(self) -> None:
        """Makes sure that visitName() bins its data in one hot vectors"""
        data = ["Mr. Jack", "Jackie Miss", "John Col James", "Nothing"]
        passengers = self.categorizedDataVisitor.visitName(data)
        self.assertEquals(len(data), len(passengers))
        self.checkOneHotEncodingOfPassengers(passengers)

    def testVisitSex(self)  -> None:
        """Makes sure that visitSex() bins its data in one hot vectors"""
        data = ["female", "female", "female", "male"]
        passengers = self.categorizedDataVisitor.visitSex(data)
        self.assertEquals(len(data), len(passengers))
        self.checkOneHotEncodingOfPassengers(passengers)

    def testVisitAge(self)  -> None:
        """Makes sure that visitAge() bins its data in one hot vectors"""
        data = [0.55, 12, 78, 22]
        passengers = self.categorizedDataVisitor.visitAge(data)
        self.assertEquals(len(data), len(passengers))
        self.checkOneHotEncodingOfPassengers(passengers)

    def testVisitSibSp(self)  -> None:
        """Makes sure that visitSibSp() bins its data in one hot vectors"""
        data = [5, 0, 3, 2]
        passengers = self.categorizedDataVisitor.visitSibSp(data)
        self.assertEquals(len(data), len(passengers))
        self.checkOneHotEncodingOfPassengers(passengers)

    def testVisitParch(self)  -> None:
        """Makes sure that visitParch() bins its data in one hot vectors"""
        data = [4, 1, 0, 6]
        passengers = self.categorizedDataVisitor.visitParch(data)
        self.assertEquals(len(data), len(passengers))
        self.checkOneHotEncodingOfPassengers(passengers)

    def testVisitTicket(self)  -> None:
        """Makes sure that visitTicket() bins its data in one hot vectors"""
        data = [300000, "PP 4348", "A/5 21173", 151003]
        passengers = self.categorizedDataVisitor.visitTicket(data)
        self.assertEquals(len(data), len(passengers))
        self.checkOneHotEncodingOfPassengers(passengers)

    def testVisitFare(self)  -> None:
        """Makes sure that visitFare() bins its data in one hot vectors"""
        data = [22.5,  35, 7, 400]
        passengers = self.categorizedDataVisitor.visitFare(data)
        self.assertEquals(len(data), len(passengers))
        self.checkOneHotEncodingOfPassengers(passengers)

    def testVisitCabin(self)  -> None:
        """Makes sure that visitCabin() bins its data in one hot vectors"""
        data = ["D36",  "C78", np.nan, "B57 B59 B63 B66"]
        passengers = self.categorizedDataVisitor.visitCabin(data)
        self.assertEquals(len(data), len(passengers))
        self.checkOneHotEncodingOfPassengers(passengers)

    def testVisitEmbarked(self)  -> None:
        """Makes sure that visitEmbarked() bins its data in one hot vectors"""
        data = ["Q",  "Q", "C", "S"]
        passengers = self.categorizedDataVisitor.visitEmbarked(data)
        self.assertEquals(len(data), len(passengers))
        self.checkOneHotEncodingOfPassengers(passengers)

    def testString(self) -> None:
        """Tests the string representation of CategorizedDataVisitor"""
        self.assertEquals(str(self.categorizedDataVisitor), "CatVis")