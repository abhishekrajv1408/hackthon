import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
from sklearn import metrics
import math
from sklearn import linear_model


def predict1(data):
    df1 = pd.read_csv('Dataset_Hackathon.csv')
    X1 = df1.drop(['Country', 'Commodity','Flow','Category'], axis = 1)
    X = X1.drop("Frieght Cost (USD)", axis="columns")
    Y = X1["Frieght Cost (USD)"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4)
    mymodel = linear_model.LinearRegression()
    mymodel.fit(X_train, Y_train)
    pred=mymodel.predict(data)
    return pred