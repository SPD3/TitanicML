from datacategoryvisitors.processeddatabuilders.NameClassifierBuilder import NameClassifierBuilder
import unittest

class NameClassifierBuilderTest (unittest.TestCase):
    """Tests the NameClassifierBuilder"""

    def test_getTitle(self):
        """Makes sure that getTitle does find titles"""
        name = "Mrs. ldajfhgp"
        nameClassifierBuilder = NameClassifierBuilder()
        title = nameClassifierBuilder.getTitle(name)
        self.assertEquals(title, "Mrs")