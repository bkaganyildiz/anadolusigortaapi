import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import feature_selection
from sklearn.naive_bayes import GaussianNB
from recommend.models import RecommendationResult
import os

BASE_PATH = os.path.join("datasets", "tic2000")

def readData():
    '''
    reads data and returns train and test data
    '''
    global TEST_DATA
    global TRAIN_DATA
    global BASE_PATH
    TRAIN_DATA_FILENAME = str(os.path.join(BASE_PATH, 'ticdata2000.txt'))
    TEST_DATA_FILENAME = str(os.path.join(BASE_PATH, 'ticeval2000.txt'))
    EVAL_FILENAME = str(os.path.join(BASE_PATH, 'tictgts2000.txt'))

    f = open(TRAIN_DATA_FILENAME, 'rb')
    trainData = []
    for line in f.readlines():
        arr = line.strip().split('\t')
        arr = map(lambda x: int(x), arr)
        trainData.append(arr)
    f.close()

    f = open(TEST_DATA_FILENAME, 'rb')
    testData = []
    for line in f.readlines():
        arr = line.strip().split('\t')
        arr = map(lambda x: int(x), arr)
        testData.append(arr)
    f.close()


    f = open(EVAL_FILENAME, 'rb')
    for index, val in enumerate(f.readlines()):
        val = int(val)
        testData[index].append(val)
    f.close()
    return trainData, testData


def getDataAndLabels(data):
    retData = []
    retLabels = []
    for row in data:
        retData.append(row[:-1])
        retLabels.append(row[-1])
    return np.array(retData), np.array(retLabels)

def featureSelection(data, labels, n):
    fvalue, pvalue = feature_selection.f_classif(np.asmatrix(np.array(data)), labels)
    fvalue_mask = fvalue > np.sort(fvalue)[fvalue.shape[0] - n]
    selectedFeatures = []
    for index, flag in enumerate(fvalue_mask):
        if flag:
            selectedFeatures.append(index)
    return selectedFeatures

def createNewDataFromSelectedFeatures(data, indexes):
    sortedIndexes = sorted(indexes)
    return data[:, sortedIndexes]

def normalizeData(data):
    x = data * 1.0
    x_normed = x / x.max(axis=0)
    return list(x_normed)

def predictionSystem(inp_trainData, inp_testData):
    _trainData, trainLabels = getDataAndLabels(inp_trainData)
    _testData, testLabels = getDataAndLabels(inp_testData)

    numberOfFeatures = range(10, 70, 10)
    mlp_scores = []
    bayes_scores = []
    dt_scores = []
    for numberOfFeature in numberOfFeatures:
        # Feature selection
        selectedFeaturesIndexes = featureSelection(_trainData, trainLabels, numberOfFeature)
        # Creating new train and test data
        trainData = createNewDataFromSelectedFeatures(_trainData, selectedFeaturesIndexes)
        testData = createNewDataFromSelectedFeatures(_testData, selectedFeaturesIndexes)
        # Normalization
        trainData = normalizeData(trainData)
        testData = normalizeData(testData)
        ret = predictionSystem_Helper(trainData, trainLabels, testData, testLabels, type=1)
        mlp_scores.append(ret)
        ret = predictionSystem_Helper(trainData, trainLabels, testData, testLabels, type=2)
        bayes_scores.append(ret)
        ret = predictionSystem_Helper(trainData, trainLabels, testData, testLabels, type=3)
        dt_scores.append(ret)

    nameList = ["accuracy", "specificity", "sensitivity", "tp"]
    retDict = {}
    RecommendationResult.objects.all().delete()
    for index, name in enumerate(nameList):
        bayes_values = map(lambda x: x[index], bayes_scores)
        mlp_values = map(lambda x: x[index], mlp_scores)
        dt_values = map(lambda x: x[index], dt_scores)
        print "len(bayes_values): ", len(bayes_values)
        print "len(mlp_values): ", len(mlp_values)
        print "len(dt_values): ", len(dt_values)
        print "len(numberOfFeatures): ", len(numberOfFeatures)
        print "numberOfFeatures: ", numberOfFeatures
        print "name: ", name
        picture = drawPrediction(name, bayes_values, mlp_values, dt_values, numberOfFeatures)
        result = RecommendationResult()
        result.set_mlp(mlp_values)
        result.set_features(numberOfFeatures)
        result.set_dt(dt_values)
        result.set_bayes(bayes_values)
        result.name = name
        result.picture = picture
        result.save()

def drawPrediction(y_name, y_1, y_2, y_3, x_values):
    import matplotlib
    matplotlib.use("qt4agg")
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    algorithm = ['Bayes'] * 6 + ['NN'] * 6 + ['Decision Tree'] * 6
    d = {y_name: y_1 + y_2 + y_3, 'Number of Features': x_values * 3, 'Algorithm': algorithm}
    df = pd.DataFrame(data=d)
    plt.subplots(figsize=(25, 15))
    plt.title('# of Features vs %s' % y_name.title(), fontsize=30)
    sns.set(font_scale=2)
    sns.pointplot(x='Number of Features', y=y_name, hue="Algorithm", data=df)
    plt.savefig('prediction.png', transparent=False)
    with open("prediction.png", "rb") as f:
        data = f.read()
        encodedString = data.encode("base64")
        return encodedString

def predictionSystem_Helper(trainData, trainLabels, testData, testLabels, type=1):
    if type == 1:
        clf = MLPClassifier(verbose=False, solver='sgd', alpha=1e-5, hidden_layer_sizes=(50,), random_state=1, max_iter=200)
    elif type == 2:
        clf = GaussianNB()
    else:
        clf = DecisionTreeClassifier()

    clf.fit(trainData, trainLabels)

    predictionResults = clf.predict(testData)
    tp, fp, tn, fn = 0, 0, 0, 0
    accuracy = 0
    for i in range(len(testLabels)):
        if int(testLabels[i]) == 1 and int(predictionResults[i]) == 1:
            tp += 1
        elif int(testLabels[i]) == 1 and int(predictionResults[i]) == 0:
            fn += 1
        elif int(testLabels[i]) == 0 and int(predictionResults[i]) == 0:
            tn += 1
        elif int(testLabels[i]) == 0 and int(predictionResults[i]) == 1:
            fp += 1

        if int(testLabels[i]) == int(predictionResults[i]):
            accuracy += 1

    accuracy = float(tp + tn) / float(tp + fp + tn + fn)
    sensitivity = float(tp) / float(tp + fn)
    specificity = float(tn) / float(fp + tn)

    print "type: ", type
    print "accuracy: ", accuracy
    print "sensitivity: ", sensitivity
    print "specificity: ", specificity
    print "tp: ", tp
    print "list(predictionResults[i]).count(1): ", list(predictionResults).count(1)
    print "testLabels.count(1): ", list(testLabels).count(1)
    return accuracy, specificity, sensitivity, tp


trainData, testData = readData()

predictionSystem(trainData, testData)
