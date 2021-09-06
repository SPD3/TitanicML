import unittest
from datacategoryvisitors.processeddatabuilders.BinarySexDataBuilder import BinarySexDataBuilder

class BinarySexDataBuilderTest (unittest.TestCase):
    """Tests the BinarySexDataBuilder class"""  
    def setUp(self) -> None:
        self.ageClassifierBuilder = BinarySexDataBuilder()
        
