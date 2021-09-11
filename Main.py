from endtoenditerators.AllModelCombinationsIterator import AllModelCombinationsIterator
from typing import Tuple
from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
from datacategoryvisitors.CategorizedDataVisitor import CategorizedDataVisitor
from preprocessdata.DataPreProcessorWithVisitor import DataPreProcessorWithVisitor
from datacategoryvisitors.ScaledDataCategoryVisitor import ScaledDataCategoryVisitor
import pandas as pd
from endtoendfactories.EndToEndFactoryV1 import EndToEndFactoryV1
import csv
import tensorflow as tf
import numpy as np

"""
This is the main flow control of this Titanic project. The data 
dataPreProcessor(s) is specified here and so is the model(s)
The model is trained on the data that is processed and saved away to the 
checkpoint_path path.
"""

def getListOfAllModels(dataCategoryVisitors:list, modelSizes:list[Tuple], trainData:np.ndarray) -> list[Tuple]:
    allModels = []
    for dataCategoryVisitor in dataCategoryVisitors:
        for (layerSize,layers) in modelSizes:
            dataPreProcessor = DataPreProcessorWithVisitor(trainData, True, dataCategoryVisitor)
            _, X = dataPreProcessor.getProcessedData()
            modelGenerator = RectangularDenseModelGenerator(len(X[0]), "ComparisonModel", layerSize=layerSize, layers=layers)
            allModels.append((dataCategoryVisitor, modelGenerator))
    return allModels
    
def saveModelData(names: list[str], histories:list[tf.keras.callbacks.History]) -> None:
    accFile = open("data/AllModelsAccuracy.csv", "w")
    writer = csv.writer(accFile)

    header = ["Epoch"]
    for name in names:
        header.append(name + "Acc")
    writer.writerow(header)

    epochs = len(histories[0].history["accuracy"])
    for i in range(epochs):
        line = [i]
        for history in histories:
            acc = history.history["accuracy"][i]
            line.append(acc)
        writer.writerow(line)

    accFile.close()
    
    #File for ValAcc
    valAccFile = open("data/AllModelsValAccuracy.csv", "w")
    writer = csv.writer(valAccFile)

    header = ["Epoch"]
    for name in names:
        header.append(name + "ValAcc")
    writer.writerow(header)

    epochs = len(histories[0].history["val_accuracy"])
    for i in range(epochs):
        line = [i]
        for history in histories:
            valAcc = history.history["val_accuracy"][i]
            line.append(valAcc)
        writer.writerow(line)

    valAccFile.close()

def compareAllModels(models:list[Tuple], trainData:np.ndarray)-> None:
    names = []
    histories = []
    modelNumber = 1
    for (dataCategoryVisitor, modelGenerator) in models:
        dataPreProcessor = DataPreProcessorWithVisitor(trainData, True, dataCategoryVisitor)
        y, X = dataPreProcessor.getProcessedData()
        history = modelGenerator.fitModel(X, y)
        names.append(str(modelNumber))
        histories.append(history)
        modelNumber = modelNumber + 1
    saveModelData(names, histories)

if( __name__ == "__main__"):
    print("Starting")
    train_data = pd.read_csv("titanic/train.csv")
    train_data = train_data.to_numpy().tolist()
    
    dataCategoryVisitors = [
        ScaledDataCategoryVisitor(),
        CategorizedDataVisitor()
    ]
    dataProcessorsWithVisitors = [
        DataPreProcessorWithVisitor(train_data, True)
    ]
    modelGenerators = [
        RectangularDenseModelGenerator(),
        RectangularDenseModelGenerator(layerSize=1024, layers=10)
    ]

    allModelCombinationsIterator = AllModelCombinationsIterator(dataCategoryVisitors, dataProcessorsWithVisitors, modelGenerators)
    for y, X, modelGenerator in allModelCombinationsIterator:
        history = modelGenerator.fitModel(X, y)
        
    print("All Done")

