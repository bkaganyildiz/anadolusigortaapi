import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import base64
import seaborn as sns

class recommend_utils():
    @staticmethod
    def getCorrelationMatrix(train_data,y_indexes,x_indexes):
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
        with open("correlation.png", "rb") as f:
            data = f.read()
            encodedString =  data.encode("base64")
            return encodedString

    @staticmethod
    def getCountPlot(train_data,x):
        plt.subplots(figsize=(25,15))
        sns.countplot(x=train_data.columns[x], data=train_data);
        plt.savefig('count.png')
        with open("count.png", "rb") as f:
            data = f.read()
            encodedString =  data.encode("base64")
            return encodedString

    @staticmethod
    def getViolinPlot(train_data,x,y):
        plt.subplots(figsize=(25,15))
        plt.title(train_data.columns[x] + ' vs ' + train_data.columns[y])
        sns.violinplot(x=train_data.columns[x], y=train_data.columns[y], data=train_data,split=True);
        plt.savefig('violin.png')
        with open("violin.png", "rb") as f:
            data = f.read()
            encodedString =  data.encode("base64")
            return encodedString