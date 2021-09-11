from endtoenditerators.AllModelCombinationsIterator import AllModelCombinationsIterator
from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
from datacategoryvisitors.CategorizedDataVisitor import CategorizedDataVisitor
from dataprocessors.DataProcessorWithVisitor import DataProcessorWithVisitor
from datacategoryvisitors.ScaledDataCategoryVisitor import ScaledDataCategoryVisitor
import pandas as pd
from utilities.savehistories.SaveAccAndValAccSeperateFiles import SaveAccAndValAccSeperateFiles

"""
This is the main flow control of this Titanic project. The data 
dataPreProcessor(s) is specified here and so is the model(s)
The model is trained on the data that is processed and saved away to the 
checkpoint_path path.
"""
    

if( __name__ == "__main__"):
    print("Starting")
    train_data = pd.read_csv("titanic/train.csv")
    train_data = train_data.to_numpy().tolist()
    
    dataCategoryVisitors = [
        #ScaledDataCategoryVisitor(),
        CategorizedDataVisitor()
    ]
    dataProcessorsWithVisitors = [
        DataProcessorWithVisitor(train_data, True)
    ]
    modelGenerators = [
        RectangularDenseModelGenerator(layerSize=512, layers=20),
        RectangularDenseModelGenerator(layerSize=1024, layers=10),
        RectangularDenseModelGenerator(layerSize=2048, layers=5),
        RectangularDenseModelGenerator(layerSize=4096, layers=2),
    ]

    allModelCombinationsIterator = AllModelCombinationsIterator(dataCategoryVisitors, dataProcessorsWithVisitors, modelGenerators)
    saveAccAndValAccSeperateFiles = SaveAccAndValAccSeperateFiles("Models")
    for y, X, modelGenerator, name in allModelCombinationsIterator:
        history = modelGenerator.fitModel(X, y)
        saveAccAndValAccSeperateFiles.addHistory(history, name)
    saveAccAndValAccSeperateFiles.saveAddedHistories()

    print("All Done")

