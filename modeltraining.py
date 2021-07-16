# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 19:58:37 2021

@author: Asus
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data=pd.read_csv('Tdata.csv')
X=data[['Year','Month']]
Y=data['Value']

regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, Y)


# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(int(model.predict([[0.95,0]])[0]))