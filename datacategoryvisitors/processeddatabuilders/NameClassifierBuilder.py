from datacategoryvisitors.processeddatabuilders.ProcessedDataBuilderBase \
    import ProcessedDataBuilderBase

class NameClassifierBuilder (ProcessedDataBuilderBase):
    """Classifies each passengers name based on title"""

    def buildProcessedData(self) -> None:
        """Looks through each passenger's name and categorizes it"""
        for name in self.preprocessedData:
            title = self.getTitle(name)
            self.initializeNameMapping()
            self.mapTitle(title)
            self.processedData.append(self.currentNameMapping)

    def getTitle(self, name: str) -> str:
        """Gets the first title that is found within a name"""
        title_list=['Mrs', 'Mr', 'Master', 'Miss', 'Major', 'Rev',
                    'Dr', 'Ms', 'Mlle','Col', 'Capt', 'Mme', 'Countess',
                    'Don', 'Jonkheer']
        for title in title_list:
            if title in name:
                return title
        return "None"

    def initializeNameMapping(self) -> None:
        """Initializes a nameMapping with 5 bins"""
        self.currentNameMapping = []
        for i in range(5):
            self.currentNameMapping.append(0.0)
    
    def mapTitle(self, title) -> None:
        """Maps a title to a bin"""
        if(title in ['Don', 'Major', 'Capt', 'Jonkheer', 'Rev', 'Col']):
            self.currentNameMapping[0] = 1.0
        elif(title in ['Countess', 'Mme']):
            self.currentNameMapping[1] = 1.0
        elif(title in ['Mlle', 'Ms']):
            self.currentNameMapping[2] = 1.0
        elif(title in ['Dr']):
            self.currentNameMapping[3] = 1.0
        else:
            self.currentNameMapping[4] = 1.0