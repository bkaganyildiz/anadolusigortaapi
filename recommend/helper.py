"""
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import base64
import seaborn as sns
"""
import itertools
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import feature_selection
from sklearn.naive_bayes import GaussianNB

class recommend_utils():
    @staticmethod
    def getCorrelationMatrix(train_data,y_indexes,x_indexes):
        import matplotlib.pyplot as plt
        import seaborn as sns
        sns.set(font_scale=2)
        corr = train_data.corr()
        y_final = []
        for index in y_indexes:
            y_final.append(corr.columns[index])
        plt.subplots(figsize=(25,20))
        plt.title('Correlation of Features', fontsize=25)
        abc = sns.heatmap(corr[y_final].iloc[x_indexes],
                    xticklabels=corr.columns[y_indexes],
                    yticklabels= corr.columns[x_indexes],
                    annot=True,
                     linewidths=.5,
                     square=True,
                     cmap="Blues")
        plt.savefig('correlation.png')
        plt.clf()
        plt.close()
        plt.close('all')

        with open("correlation.png", "rb") as f:
            data = f.read()
            encodedString =  data.encode("base64")
            return encodedString

    @staticmethod
    def getCountPlot(train_data,x):
        import matplotlib.pyplot as plt
        import seaborn as sns
        sns.set(font_scale=2)
        plt.subplots(figsize=(25,15))
        plt.title('Occurence of' + train_data.columns[x], fontsize=25)
        sns.countplot(x=train_data.columns[x], data=train_data)
        plt.savefig('count.png')
        with open("count.png", "rb") as f:
            data = f.read()
            encodedString = data.encode("base64")
            return encodedString

    @staticmethod
    def getViolinPlot(train_data,descriptions, x,y):
        import matplotlib
        matplotlib.use("qt4agg")
        import matplotlib.pyplot as plt
        import seaborn as sns
        sns.set(font_scale=2)
        plt.subplots(figsize=(25,15))
        plt.title(str(descriptions[x]) + ' vs ' + str(descriptions[y]),fontsize=25)
        sns.barplot(x=train_data.columns[x], y=train_data.columns[y], data=train_data, ci=None)
        plt.savefig('violin.png')
        with open("violin.png", "rb") as f:
            data = f.read()
            encodedString = data.encode("base64")
            return encodedString

    @staticmethod
    def lenFinder(train_data_x, indexes):
        if indexes == []:
            return len(train_data_x)
        else:
            train_data_new = train_data_x.loc[(train_data_x[train_data_x.columns[indexes[0]]] >= 1)]
            return recommend_utils.lenFinder(train_data_new, indexes[1:])

    @staticmethod
    def getCombinations(lst):
        combs = []
        for i in xrange(1, len(lst) + 1):
            els = [list(x) for x in itertools.combinations(lst, i)]
            combs = combs + els
        return combs

    @staticmethod
    def associationFinder(train_data, lhs, minSupport):
        rules = []
        N = 4000.0
        combs = recommend_utils.getCombinations(lhs)
        all_values = range(64, 85)
        for item_left in combs:
            divider = recommend_utils.lenFinder(train_data, item_left) * 1.0
            if divider != 0:
                for item_all in all_values:
                    if item_all in lhs:
                        continue
                    else:
                        lhs_plus_rhs = item_left + [item_all]
                        support_head = recommend_utils.lenFinder(train_data, [item_all]) / N
                        support = recommend_utils.lenFinder(train_data, lhs_plus_rhs) / N
                        if minSupport < support:
                            confidence = recommend_utils.lenFinder(train_data, lhs_plus_rhs) / divider
                            association = {
                                'source': item_left,
                                'dest': item_all,
                                'support': support,
                                'confidence': confidence,
                                'lift': confidence / support_head
                            }
                            rules.append(association)
        sorted_rules = sorted(rules, key=lambda k: k['confidence'], reverse=True)
        return sorted_rules

    @staticmethod
    def getDataAndLabels(data):
        retData = []
        retLabels = []
        for row in data:
            retData.append(row[:-1])
            retLabels.append(row[-1])
        return np.array(retData), np.array(retLabels)

    @staticmethod
    def featureSelection(data, labels, n):
        fvalue, pvalue = feature_selection.f_classif(np.asmatrix(np.array(data)), labels)
        fvalue_mask = fvalue > np.sort(fvalue)[fvalue.shape[0] - n]
        selectedFeatures = []
        for index, flag in enumerate(fvalue_mask):
            if flag:
                selectedFeatures.append(index)
        return selectedFeatures

    @staticmethod
    def createNewDataFromSelectedFeatures(data, indexes):
        sortedIndexes = sorted(indexes)
        return data[:, sortedIndexes]

    @staticmethod
    def normalizeData(data):
        x = data * 1.0
        x_normed = x / x.max(axis=0)
        return list(x_normed)

    @staticmethod
    def predictionSystem(inp_trainData, inp_testData, numberOfFeatures):
        _trainData, trainLabels = recommend_utils.getDataAndLabels(inp_trainData)
        _testData, testLabels = recommend_utils.getDataAndLabels(inp_testData)

        numberOfFeatures = range(10, 70, 10)
        mlp_scores = []
        bayes_scores = []
        dt_scores = []
        for numberOfFeature in numberOfFeatures:
            # Feature selection
            selectedFeaturesIndexes = recommend_utils.featureSelection(_trainData, trainLabels, numberOfFeature)
            # Creating new train and test data
            trainData = recommend_utils.createNewDataFromSelectedFeatures(_trainData, selectedFeaturesIndexes)
            testData = recommend_utils.createNewDataFromSelectedFeatures(_testData, selectedFeaturesIndexes)
            # Normalization
            trainData = recommend_utils.normalizeData(trainData)
            testData = recommend_utils.normalizeData(testData)
            ret = recommend_utils.predictionSystem_Helper(trainData, trainLabels, testData, testLabels, type=1)
            mlp_scores.append(ret)
            ret = recommend_utils.predictionSystem_Helper(trainData, trainLabels, testData, testLabels, type=2)
            bayes_scores.append(ret)
            ret = recommend_utils.predictionSystem_Helper(trainData, trainLabels, testData, testLabels, type=3)
            dt_scores.append(ret)

        nameList = ["accuracy", "specificity", "sensitivity", "tp"]
        retDict = {}
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
            retDict[name] = recommend_utils.drawPrediction(name, bayes_values, mlp_values, dt_values, numberOfFeatures)

        return retDict

    @staticmethod
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
        plt.savefig('prediction.png')
        with open("prediction.png", "rb") as f:
            data = f.read()
            encodedString = data.encode("base64")
            return encodedString

    @staticmethod
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

