import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
class Oxypred:

    def __init__(self,val):
        self.data = pd.read_csv('D:\IOE\IOE - Sheet1.csv')
        x = self.data.iloc[:,5]
        y = self.data.iloc[:,-1]
        for i in range(len(x)-1):
            x[i] -= x[i+1] 
        for i in range(len(x)):
            x[i] %= 100
        for i in range(len(y)):
            y[i] = x[i]*7.5
        xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=0)  
        self.model = LinearRegression() 
        self.model.fit(np.array(xtrain).reshape(-1,1),np.array(ytrain))
    def predict(self,val):
        return self.model.predict([[val]])
    