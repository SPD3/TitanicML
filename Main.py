from modelgenerators.RectangularDenseModelGenerator import RectangularDenseModelGenerator
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

train_data = pd.read_csv("titanic/train.csv")
train_data = train_data.to_numpy()

visitor = CategorizedDataVisitor()
dataPreProcessor = DataPreProcessorWithVisitor(train_data, True, visitor)
y, X = dataPreProcessor.getProcessedData()

myModel = RectangularDenseModelGenerator(len(X[0]))

if( __name__ == "__main__"):
    
    myModel.fitModel(X, y, checkpoint_path)


