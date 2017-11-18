"""
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import base64
import seaborn as sns
"""
import itertools

class recommend_utils():
    @staticmethod
    def getCorrelationMatrix(train_data,y_indexes,x_indexes):
        import matplotlib.pyplot as plt
        import seaborn as sns
        corr = train_data.corr()
        y_final = []
        for index in y_indexes:
            y_final.append(corr.columns[index])
        plt.subplots(figsize=(25,20))
        plt.title('Correlation of Features')
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
        plt.subplots(figsize=(25,15))
        sns.countplot(x=train_data.columns[x], data=train_data)
        plt.savefig('count.png')
        with open("count.png", "rb") as f:
            data = f.read()
            encodedString =  data.encode("base64")
            return encodedString

    @staticmethod
    def getViolinPlot(train_data,descriptions, x,y):
        import matplotlib
        matplotlib.use("qt4agg")
        import matplotlib.pyplot as plt
        import seaborn as sns
        plt.subplots(figsize=(25,15))
        plt.title(str(descriptions[x]) + ' vs ' + str(descriptions[y]))
        sns.violinplot(x=train_data.columns[x], y=train_data.columns[y], data=train_data,split=True)
        plt.savefig('violin.png')
        with open("violin.png", "rb") as f:
            data = f.read()
            encodedString =  data.encode("base64")
            return encodedString,

    @staticmethod
    def lenFinder(train_data_x, indexes):
        if indexes == []:
            return len(train_data_x)
        else:
            train_data_new = train_data_x.loc[(train_data[train_data.columns[indexes[0]]] >= 1)]
            return lenFinder(train_data_new, indexes[1:]),

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
        combs = getCombinations(lhs)
        all_values = range(43, 85)
        for item_left in combs:
            divider = lenFinder(train_data, item_left) * 1.0
            if divider != 0:
                for item_all in all_values:
                    if item_all in lhs:
                        continue
                    else:
                        lhs_plus_rhs = item_left + [item_all]
                        support = lenFinder(train_data, lhs_plus_rhs) / N
                        if minSupport < support:
                            confidence = lenFinder(train_data, lhs_plus_rhs) / divider
                            association = {
                                'source': item_left,
                                'dest': item_all,
                                'support': support,
                                'confidence': confidence
                            }
                            rules.append(association)
        sorted_rules = sorted(rules, key=lambda k: k['confidence'], reverse=True)
        return sorted_rules