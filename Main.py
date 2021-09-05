from modelgenerators.SimpleDenseModelGenerator import SimpleDenseModelGenerator
from datacategoryvisitors.CategorizedDataVisitor import CategorizedDataVisitor
from preprocessdata.DataPreProcessorWithVisitor import DataPreProcessorWithVisitor
import pandas as pd

"""
This is the main flow control of this Titanic project. The data 
dataPreProcessor(s) is specified here and so is the model(s)
The model is trained on the data that is processed and saved away to the 
checkpoint_path path.
"""
name = "Model1"
checkpoint_path = "savedmodels/" + name + "cp.ckpt1"

if( __name__ == "__main__"):
    train_data = pd.read_csv("/Users/seandoyle/git/TitanicML/titanic/train.csv")
    train_data = train_data.to_numpy()

    visitor = CategorizedDataVisitor()
    dataPreProcessor = DataPreProcessorWithVisitor(train_data, True, visitor)
    y, X = dataPreProcessor.getProcessedData()

    myModel = SimpleDenseModelGenerator(len(X[0]))
    myModel.fitModel(X, y, checkpoint_path)


