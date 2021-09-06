import unittest
from datacategoryvisitors.processeddatabuilders.AgeClassifierBuilder import AgeClassifierBuilder

class AgeClassifierBuilderTest (unittest.TestCase):
    """Tests the AgeClassifierBuilder class"""
    def setUp(self) -> None:
        self.ageClassifierBuilder = AgeClassifierBuilder()

    def testInitializeAgeMapping(self) -> None:
        self.ageClassifierBuilder.initializeAgeMapping()
        self.assertEquals(type(self.ageClassifierBuilder.currentAgeMapping), list)
        for value in self.ageClassifierBuilder.currentAgeMapping:
            self.assertEquals(value, 0.0)
        
