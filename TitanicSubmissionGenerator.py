import Main
import pandas as pd
import csv

if( __name__ == "__main__"):
    factory = Main.factory
    checkpoint_path = Main.checkpoint_path

    test_data = pd.read_csv("/Users/seandoyle/git/TitanicML/titanic/test.csv")
    test_data = test_data.to_numpy()

    _, X = factory.getDataPreProcessorType()(test_data, False).getProcessedData()
    
    modelGenerator = factory.getModelType()(len(X[0]))
    modelGenerator.createModel()
    model = modelGenerator.getModel()
    model.load_weights(checkpoint_path)

    predictions = model.predict(X)

    f = open("submissions/submission1.csv", "w")
    writer = csv.writer(f)

    header = ["PassengerId", "Survived"]
    writer.writerow(header)

    currentId = 892
    for prediction in predictions:
        if(prediction[0] > 0.5):
            nextLine = [currentId, 1]
        else:
            nextLine = [currentId, 0]
        currentId += 1
        writer.writerow(nextLine)

    f.close()
    print("All done!")
