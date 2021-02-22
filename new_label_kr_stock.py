# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 14:48:19 2021

@author: user
"""

import glob
import os
import pandas as pd
import  talib
import numpy as np

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

path = "C:/Users/user/Desktop/연구/시가총액100위"

file_list =os.listdir(path)

df= []

for file in file_list:
    path = "C:/Users/user/Desktop/연구/시가총액100위"
    
    df.append(pd.read_csv(path+"/"+file))


for  i in df:
    ADX=talib.ADX(i.High,i.Low,i.Close,timeperiod=14)
 
    aroondown,aroonup =talib.AROON(i.High, i.Low, timeperiod=14)
    
    AROONOSC=talib.AROONOSC(i.High,i.Low,timeperiod=14)
    
    BOP=talib.BOP(i.Open,i.High,i.Low,i.Close)
    
    CCI=talib.CCI(i.High,i.Low,i.Close,timeperiod=9)
    
    CMO=talib.CMO(i.Close,timeperiod=14)
    
    DX=talib.DX(i.High,i.Low,i.Close,timeperiod=14)
    
    MFI=talib.MFI(i.High, i.Low,i.Close, i.Volume, timeperiod=14)
    
    PPO=talib.PPO(i.Close, fastperiod=12, slowperiod=26, matype=0)
    
    ROC=talib.ROC(i.Close,timeperiod=10)
    
    RSI=talib.RSI(i.Close,timeperiod=14)
    
    slowk, slowd = talib.STOCH(i.High, i.Low, i.Close, fastk_period=12.5, slowk_period=5, slowk_matype=0, slowd_period=3, slowd_matype=0)
    
    fastk, fastd = talib.STOCHF(i.High, i.Low, i.Close, fastk_period=5, fastd_period=5.3, fastd_matype=0)
    
    ULTOSC=talib.ULTOSC(i.High,i.Low,i.Close,timeperiod1=7,timeperiod2=14,timeperiod3=28)
    
    WILLR=talib.WILLR(i.High,i.Low,i.Close,timeperiod=14)
        
    i['ADX']=ADX
    i['aroondown']=aroondown
    i['aroonup']=aroonup
    i['BOP']=BOP
    i['CCI']=CCI
    i['CMO']=CMO
    i['DX']=DX
    i['MFI']=MFI
    i['PPO']=PPO
    i['ROC']=ROC
    i['RSI']=RSI
    i['slowk']=slowk
    i['slowd']=slowd
    i['fastk']=fastk
    i['fastd']=fastd
    i['ULTOSC']=ULTOSC
    i['WILLR']=WILLR


for i in df:
    i['diff']=i.Close.diff().shift(-1).fillna(0)
    i['Label'] = None
    i['return'] = None
    

for i in df:
    i=i.drop(['Unnamed: 0'],axis=1)



#수익률 표준편차 계산

for i in df:
    i['return']=i['Close'].pct_change()*100



   

train_data=[]



test_data=[]


for i in range(0,75):
    train=df[i]['Date'].str.contains('2009|2010|2011|2012|2013|2014|2015|2016|2017|2018|2019')
    train_data.append(df[i][train])
for i in range(0,75):    
    test=df[i]['Date'].str.contains('2020')
    test_data.append(df[i][test])


#train set std_return
std_return =[]

len(std_return)


for i in train_data:    
    std_return.append(np.std(i['return']))


#up/down 기준 생성 
up_label =[]
down_label= []

for i in len(std_return):
    up_label.append(0.5*std_return[i])
    down_label.append(-0.5 * std_return[i])
    
    

#label 생성

for i in train_data:
    for e in range(len(i['diff'])):
        if i['return'][e] > 
