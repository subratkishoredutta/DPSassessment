# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 15:44:04 2021

@author: Asus
"""

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('data.csv')
data=data.rename(columns={'MONATSZAHL':"Category", 'AUSPRAEGUNG':'Accident_type', 'JAHR':"Year", 'MONAT':"Month", 'WERT':'Value'})

data=data[['Category','Accident_type','Year','Month','Value']]
newdata = pd.DataFrame()

for i in range(len(data)):
    if data.loc[i]['Month'] != "Summe" and data.iloc[i]["Year"]!=2021:
        newdata=newdata.append(data.loc[i])
        

types=newdata.Category.unique()
counts={types[0]:0,types[1]:0,types[2]:0}

for accitype in types:
    for i in range(len(newdata)):
        if newdata.iloc[i]['Category']==accitype:
            counts[accitype]+=newdata.iloc[i]['Value']

values = list(counts.values())
  
fig = plt.figure(figsize = (20, 10))
 
# creating the bar plot
plt.bar(types, values, color =['orange','cyan','red'],
        width = 0.4)
plt.xlabel("Category")
plt.ylabel("Number of accidents")
plt.title("number of accidents from each type from the year 2000-2020")
plt.show()
plt.savefig('20years.png')

countsPY={
         2000:0,2001:0,2002:0,2003:0,2004:0,2005:0,2006:0,2007:0,2008:0,2009:0,2010:0,2011:0,2012:0,2013:0,2014:0,2015:0,2016:0,2017:0,2018:0,2019:0,2020:0
         }

##for type 0

for j in range(2000,2021,1):
    for i in range(len(newdata)):
        if newdata.iloc[i]['Year']==j and data.iloc[i]['Category']==types[0]:
            countsPY[j]+=int(newdata.iloc[i]['Value'])

years=['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']

valuesT1=list(countsPY.values())

fig = plt.figure(figsize = (20, 10))
plt.plot(years,valuesT1,marker='o',label=types[0],color='cyan')
plt.xlabel("Category")
plt.ylabel("Number of accidents")
plt.title("number of accidents from type "+types[0]+"  from the year 2000-2020")
plt.legend()
plt.show()
plt.savefig('T120years.png')

countsPY={
         2000:0,2001:0,2002:0,2003:0,2004:0,2005:0,2006:0,2007:0,2008:0,2009:0,2010:0,2011:0,2012:0,2013:0,2014:0,2015:0,2016:0,2017:0,2018:0,2019:0,2020:0
         }

##for type 1

for j in range(2000,2021,1):
    for i in range(len(newdata)):
        if newdata.iloc[i]['Year']==j and data.iloc[i]['Category']==types[1]:
            countsPY[j]+=int(newdata.iloc[i]['Value'])

valuesT1=list(countsPY.values())

fig = plt.figure(figsize = (20, 10))
plt.plot(years,valuesT1,marker='o',label=types[1],color='cyan')
plt.xlabel("Category")
plt.ylabel("Number of accidents")
plt.title("number of accidents from type "+types[1]+"  from the year 2000-2020")
plt.legend()
plt.show()
plt.savefig('T220years.png')


##for type 2

for j in range(2000,2021,1):
    for i in range(len(newdata)):
        if newdata.iloc[i]['Year']==j and data.iloc[i]['Category']==types[2]:
            countsPY[j]+=int(newdata.iloc[i]['Value'])

valuesT1=list(countsPY.values())

fig = plt.figure(figsize = (20, 10))
plt.plot(years,valuesT1,marker='o',label=types[2],color='cyan')
plt.xlabel("Category")
plt.ylabel("Number of accidents")
plt.title("number of accidents from type "+types[2]+" from the year 2000-2020")
plt.legend()
plt.show()
plt.savefig('T320years.png')
