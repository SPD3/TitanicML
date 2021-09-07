from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase import ProcessedDataBuilderBase

class TicketClassifierBuilder (ProcessedDataBuilderBase):
    """Classify tickets based on their number and/or their names"""

    def _buildProcessedData(self) -> None:
        """Looks through each ticket for each passenger and classifies it into 
        a bin"""
        for ticket in self._preprocessedData:
            self._initializeCurrentTicketMapping()
            try:
                self._mapTicketBasedOnNumber(ticket)
            except:
                # This means the ticket is not just a number, it has letters 
                # in it
                self._mapTicketBasedOnLetters(ticket)
            
            self._processedData.append(self._currentTicketMapping)

    def _initializeCurrentTicketMapping(self) -> None:
        """Initializes the current ticket mapping with 13 bins"""
        self._currentTicketMapping = []
        for i in range(13):
            self._currentTicketMapping.append(0.0)

    def _mapTicketBasedOnNumber(self, ticket) -> None:
        """Looks at the number on a ticket and assigns it to a bin 
        accordingly"""
        ticket = int(ticket)   
        if(ticket < 100000):
            self._currentTicketMapping[0] = 1.0
        elif(ticket < 200000):
            self._currentTicketMapping[1] = 1.0
        else:
            self._currentTicketMapping[2] = 1.0

    def _mapTicketBasedOnLetters(self, ticket: str) -> None:
        """Looks at the letters on a ticket and assigns it to a bin 
        accordingly"""
        if("LINE" in ticket):
            self._currentTicketMapping[3] = 1.0
        elif("STON" in ticket):
            self._currentTicketMapping[4] = 1.0
        elif("PARIS" in ticket):
            self._currentTicketMapping[5] = 1.0
        elif("PP" in ticket):
            self._currentTicketMapping[6] = 1.0
        elif("A/5" in ticket):
            self._currentTicketMapping[7] = 1.0
        elif("SOTON" in ticket):
            self._currentTicketMapping[8] = 1.0
        elif("F.C.C." in ticket):
            self._currentTicketMapping[9] = 1.0
        elif("A" in ticket and "C" in ticket):
            self._currentTicketMapping[10] = 1.0
        elif("P" in ticket and "C" in ticket):
            self._currentTicketMapping[11] = 1.0
        else:
            self._currentTicketMapping[12] = 1.0