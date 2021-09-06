from preprocessdata.DataPreProcessorWithVisitor import DataPreProcessorWithVisitor
import pandas as pd
import csv
from endtoendfactories.EndToEndFactoryV1 import EndToEndFactoryV1

"""
This is where a submission is generated for the titanic competition once a model
has been trained. A trained model is loaded and then predictions are made on 
test data provided by the contest. These predictions are then saved into a csv
file to be submitted for grading.
"""

if( __name__ == "__main__"):
    factory = EndToEndFactoryV1.getInstance()

    test_data = pd.read_csv("titanic/test.csv")
    test_data = test_data.to_numpy()

    _, X = factory.getPreProcessData(test_data, False).getProcessedData()

    modelGenerator = factory.getModelGenerator(len(X[0]))
    model = modelGenerator.getModel()
    model.load_weights(modelGenerator.getCheckpointPath())

    predictions = model.predict(X)

    submissionName = factory.getName() + "Submission.csv"
    f = open("submissions/" + submissionName, "w")
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
