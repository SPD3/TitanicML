from endtoendfactories.SimpleFactory import SimpleFactory
import pandas as pd

if( __name__ == "__main__"):
    train_data = pd.read_csv("/Users/seandoyle/git/TensorflowTesting/titanic/train.csv")
    train_data = train_data.to_numpy()

    factory = SimpleFactory.getInstance()

    dataPreProcessor = factory.getDataPreProcessor()(train_data)
    y, X = dataPreProcessor.getProcessedData()
    
    model = factory.getModelType()(len(X[0])).createModel()


