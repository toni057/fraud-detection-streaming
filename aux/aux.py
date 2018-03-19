import numpy as np
import pandas as pd
from sklearn.metrics import auc
from sklearn.pipeline import Pipeline
from sklearn.metrics import precision_recall_curve
from dfply import dfpipe, mask, sample, bind_rows, X
import matplotlib.pyplot as plt
import seaborn as sns;



@dfpipe
def heatmap(df, annot=False, fmt='d', ax=None):
    sns.heatmap(data=df, annot=annot, cmap="YlGnBu", fmt=fmt, ax=ax)


def undersample(d, percentageFraud=0.1):
    nNewFraud = int(d.isFraud[d.isFraud==1].count() * (1-percentageFraud)/percentageFraud)

    return d >> \
        mask(X.isFraud == 0) >> \
        sample(n=nNewFraud, replace=False) >> \
        bind_rows(d[d.isFraud == 1])


class ExtractRecipientType():
    def fit(self, y):
        return
    def transform(self, y):
        for i, yi in enumerate(y):
            y[i] = yi[0]
        return y
    def fit_transform(self, y):
        return self.transform(y)

class StepToHour():
    def fit(self, y):
        return
    def transform(self, y):
        return y % 24
    def fit_transform(self, y):
        return self.transform(y)

class StepToDay():
    def fit(self, y):
        return
    def transform(self, y):
        return (y // 24) % 7
    def fit_transform(self, y):
        return self.transform(y)

class RecategorizeType():
    def fit(self, y):
        return
    def transform(self, y):
        return np.where(y != 'CASH_OUT',
                        np.where(y != 'TRANSFER', "OTHER", y),
                        y)
    def fit_transform(self, y):
        return self.transform(y)

class predictClass():
    def __init__(self, pipeline, threshold):
        self.pipeline = pipeline
        self.threshold = threshold
    def predict(self, row):
        return ["NON_FRAUD", "FRAUD"][int(self.pipeline.predict_proba(pd.DataFrame([row]))[0][1] > self.threshold)]





def plotPrecRecCurve(precision, recall, subset):
    plt.step(recall, precision, color='b', alpha=0.2,
             where='post')
    plt.fill_between(recall, precision, step='post', alpha=0.2,
                     color='b')

    aucPrecRec = auc(recall, precision)

    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall curve %s data, AUC = %0.3f' %(subset, aucPrecRec));


# def calcCost(y, d, thresh):
#     x = pd.crosstab(d.isFraud, np.where(y >= thresh, '1_Fraud', '0_nonfr'))
#     print(x)
#     return (x.as_matrix()[1,0]*10 + x.as_matrix()[0,1])
