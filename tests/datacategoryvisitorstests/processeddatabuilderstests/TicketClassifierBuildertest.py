import unittest

import numpy as np
from datacategoryvisitors.processeddatabuilders.TicketClassifierBuilder import TicketClassifierBuilder

class TicketClassifierBuilderTest (unittest.TestCase):
    """Tests the TicketClassifierBuilder class"""
    def setUp(self) -> None:
        self._ticketClassifierBuilder = TicketClassifierBuilder()

    def testInitializeCurrentTicketMapping(self) -> None:
        """Makes sure that initializeCurrentTicketMapping() creates a list 13 
        bins long and is all 0s"""
        self._ticketClassifierBuilder._initializeCurrentTicketMapping()
        self.assertEquals(type(self._ticketClassifierBuilder._currentTicketMapping), list)
        solution = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        self.assertEquals(solution, self._ticketClassifierBuilder._currentTicketMapping)

    def testMapTicketBasedOnNumber(self) -> None:
        """Makes sure that mapTicketBasedOnNumber() maps various tickets that 
        are only numbers to the correct bin"""
        def testNewTicketValue(ticket:float, solution:list[float]):
            self._ticketClassifierBuilder._initializeCurrentTicketMapping()
            self._ticketClassifierBuilder._mapTicketBasedOnNumber(ticket)
            self.assertEquals(solution, self._ticketClassifierBuilder._currentTicketMapping)

        solution =  [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        testNewTicketValue(30000, solution)

        solution = [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        testNewTicketValue(150000, solution)

        solution = [0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        testNewTicketValue(300000, solution)
    
    def testMapTicketBasedOnLetters(self) -> None:
        """Makes sure that mapTicketBasedOnLetters() maps various tickets that 
        have letters in them to the correct bin"""
        def testNewTicketValue(ticket:str, solution:list[float]):
            self._ticketClassifierBuilder._initializeCurrentTicketMapping()
            self._ticketClassifierBuilder._mapTicketBasedOnLetters(ticket)
            self.assertEquals(solution, self._ticketClassifierBuilder._currentTicketMapping)

        solution =  [0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0]
        testNewTicketValue("A/5 43402", solution)

        solution = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0]
        testNewTicketValue("F.C.C. 150000", solution)

        solution = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0]
        testNewTicketValue("ATC 4325", solution)

        solution = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0]
        testNewTicketValue("4325", solution)

    def testBuildProcessedData(self) -> None:
        """Makes sure that for every ticket passed in it is binned and appended 
        to processedData"""
        preprocessedData = [175000, "PARIS 42", "JJ 55", 5000]
        self._ticketClassifierBuilder._preprocessedData = preprocessedData
        self._ticketClassifierBuilder._buildProcessedData()
        solution = [
            [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
            [0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
            [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0],
            [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        ]
        self.assertEquals(solution, self._ticketClassifierBuilder._processedData)