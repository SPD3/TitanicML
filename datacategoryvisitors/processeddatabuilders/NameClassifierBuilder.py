from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase

class NameClassifierBuilder (ProcessedDataBuilderBase):
    """Classifies each passengers name based on title"""

    def _buildProcessedData(self) -> None:
        """Looks through each passenger's name and categorizes it"""
        for name in self._preprocessedData:
            title = self._getTitle(name)
            self._initializeNameMapping()
            self._mapTitle(title)
            self._processedData.append(self._currentNameMapping)

    def _getTitle(self, name: str) -> str:
        """Gets the first title that is found within a name"""
        title_list=['Mrs', 'Mr', 'Master', 'Miss', 'Major', 'Rev',
                    'Dr', 'Ms', 'Mlle','Col', 'Capt', 'Mme', 'Countess',
                    'Don', 'Jonkheer']
        for title in title_list:
            if title in name:
                return title
        return "None"

    def _initializeNameMapping(self) -> None:
        """Initializes a nameMapping with 5 bins"""
        self._currentNameMapping = []
        for i in range(6):
            self._currentNameMapping.append(0.0)
    
    def _mapTitle(self, title:str) -> None:
        """Maps a title to a bin"""
        if(title in ['Don', 'Major', 'Capt', 'Jonkheer', 'Rev', 'Col', "Mr"]):
            self._currentNameMapping[0] = 1.0
        elif(title in ['Countess', 'Mme', 'Mlle', 'Ms', 'Miss']):
            self._currentNameMapping[1] = 1.0
        elif(title in ['Mrs']):
            self._currentNameMapping[2] = 1.0
        elif(title in ['Dr']):
            self._currentNameMapping[3] = 1.0
        elif(title in ['Master']):
            self._currentNameMapping[4] = 1.0
        else:
            self._currentNameMapping[5] = 1.0