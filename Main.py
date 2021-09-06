from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
from datacategoryvisitors.CategorizedDataVisitor import CategorizedDataVisitor
from preprocessdata.DataPreProcessorWithVisitor import DataPreProcessorWithVisitor
import pandas as pd
from endtoendfactories.EndToEndFactoryV1 import EndToEndFactoryV1

"""
This is the main flow control of this Titanic project. The data 
dataPreProcessor(s) is specified here and so is the model(s)
The model is trained on the data that is processed and saved away to the 
checkpoint_path path.
"""


if( __name__ == "__main__"):

    train_data = pd.read_csv("titanic/train.csv")
    train_data = train_data.to_numpy()

    factory = EndToEndFactoryV1.getInstance()
    dataPreProcessor = factory.getPreProcessData(train_data, True)
    y, X = dataPreProcessor.getProcessedData()

    myModelGenerator = factory.getModelGenerator(len(X[0]))
    myModelGenerator.fitModel(X, y)


