from endtoendfactories.SimpleFactory import SimpleFactory
import pandas as pd

factory = SimpleFactory.getInstance()
checkpoint_path = "savedmodels/cp.ckpt1"

if( __name__ == "__main__"):
    train_data = pd.read_csv("/Users/seandoyle/git/TitanicML/titanic/train.csv")
    train_data = train_data.to_numpy()

    dataPreProcessor = factory.getDataPreProcessorType()(train_data)
    y, X = dataPreProcessor.getProcessedData()

    myModel = factory.getModelType()(len(X[0]))
    myModel.fitModel(X, y, checkpoint_path)





