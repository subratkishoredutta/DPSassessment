# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 16:45:35 2021

@author: Asus
"""

import pandas as pd
import sklearn
from tqdm import tqdm
data=pd.read_csv('Tdata.csv')


data=data.rename(columns={'MONATSZAHL':"Category", 'AUSPRAEGUNG':'Accident_type', 'JAHR':"Year", 'MONAT':"Month", 'WERT':'Value'})

data=data[['Year','Month','Value']]
data.dropna(subset = ["Year","Month","Value"], inplace=True)
data=data[data.Month!='Summe']

for i in tqdm(range(len(data))):
    data['Month'].iloc[i]=float(data['Month'].iloc[i][-2:])
    data['Year'].iloc[i]=data['Year'].iloc[i]-2000

feature_scale=['Year','Month']
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(data[feature_scale])
scaler.transform(data[feature_scale])
trainData = pd.concat([data['Value'].reset_index(drop=True),
                    pd.DataFrame(scaler.transform(data[feature_scale]), columns=feature_scale)],
                    axis=1)

trainData.to_csv('Tdata.csv')