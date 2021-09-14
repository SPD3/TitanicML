from dataprocessors.DataProcessorGaussAndCosine import DataProcessorGaussAndCosine
from dataprocessors.DataProcessorGaussAndOrig import DataProcessorGaussAndOrig
from dataprocessors.DataProcessorCombiner import DataProcessorCombiner
from dataprocessors.DataProcessorGaussianKernel import DataProcessorGaussianKernel
from utilities.savehistories.SaveMetricsSeperateFiles import SaveMetricsSeperateFiles
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
        ScaledDataCategoryVisitor(),
        #CategorizedDataVisitor(),
    ]
    dataProcessorsWithVisitors = [
        #DataProcessorGaussianKernel(train_data, True, sigma=1.0),
        DataProcessorGaussAndCosine(train_data, True, sigma=1.0)
    ]
    modelGenerators = [
        RectangularDenseModelGenerator(name = "V2", layerSize=1024, layers=10, epochs=120, validation_split=0.0, learningRate=5.0e-5),
    ]

    allModelCombinationsIterator = AllModelCombinationsIterator(dataCategoryVisitors, dataProcessorsWithVisitors, modelGenerators)
    metrics = [
        ("Loss", ["loss"]),
        ("Val_loss", ["val_loss"]),
        ("Accuracy", ["accuracy"]),
        ("Val_Accuracy", ["val_accuracy"]),
    ]
    saveMetricsSeperateFiles = SaveMetricsSeperateFiles(metrics, "CosComparison")
    for y, X, modelGenerator, name in allModelCombinationsIterator:
        history = modelGenerator.fitModel(X, y)
        saveMetricsSeperateFiles.addHistory(history, name)
    saveMetricsSeperateFiles.saveAddedHistories()

    print("All Done")

