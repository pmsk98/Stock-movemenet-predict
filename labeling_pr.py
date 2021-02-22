# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 13:51:08 2021

@author: user
"""
import pandas as pd
import numpy as np
import math

stock =pd.read_csv('C:/Users/user/Desktop/연구/시가총액100위/삼성전자.csv')


stock=stock[['Date','Close']]



stock['return']=stock['Close'].pct_change() *100


stock


train =stock['Date'].str.contains('2009|2010|2011|2012|2013|2014|2015|2016')


train =stock[train]


train=train.reset_index()

train=train.drop(['index'],axis=1)


#수익률 히스토그램
plt.hist(train['return'])
plt.axvline(x=0.5*std,color='r',linestyle='--',linewidth=3)
plt.axvline(x=-0.5*std,color='r',linestyle='--',linewidth=3)
plt.show


#수익률 히스토그램 그린 다음 표준편차 -0.5 ~0.5 구간 no labeling 
#0.5 이상 up
#0.5 이하 down
# up/down 분포 확인
#모멘텀 지표 붙이기 up down 


#표준편차
std=np.std(train['return'])


#up/down label 생성
up_label =0.5*std

down_label=-0.5*std

#label 컬럼 생성
train['label']=None

for i in range(len(train)):
    if train['return'] > up_label:
        train['label'][i] = 'up'
    elif train['return'] < down_label:
        train['label'][i]='down'
    else:
        None
    


for i in range(len(train)):
    if train['return'][i] > up_label :
        train['label'][i]='up'
    elif train['return'][i] < down_label:
        train['label'][i]='down'
    else:
        None
        
        
train['label'].value_counts().plot(kind='bar')
plt.title('label')
plt.show