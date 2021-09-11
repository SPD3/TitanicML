from utilities.savehistories.SaveHistoriesBase import SaveHistoriesBase

class SaveAccAndValAccSeperateFiles (SaveHistoriesBase):

    def _createFilesWithLinesToSaveDict(self) -> None:
        """Creates the _filesWithLinesToSave dictionary. Every key in the 
        dictionary is name of the file to be saved, and every value associated 
        with a key is a list of lines to save to that file
        
        Creates two files: one for accuracy, and the other for validation 
        accuracy, and then creates all the lines to go into those files
        """
        
