# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:42:07 2021

@author: Asus
"""

import uvicorn
from fastapi import FastAPI
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
model = pickle.load(open('modelo.pkl','rb'))

app= FastAPI()

@app.get('/')
def predicted(year:int,month:int):
    year=year-2000
    X=[[year,month]]
    
    prediction=int(model.predict(X)[0])
    
    return {
            'prediction': prediction
            }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)