from datacategoryvisitors.processeddatabuilders.NameClassifierBuilder import NameClassifierBuilder
import unittest

class NameClassifierBuilderTest (unittest.TestCase):

    def test_getTitle(self):
        name = "Mrs. ldajfhgp"
        title = NameClassifierBuilder.getTitle(name)
        self.assertEquals(title, "Mrs")