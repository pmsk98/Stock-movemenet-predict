# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 14:56:32 2020

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df =pd.read_csv('C:/Users/user/Desktop/연구/AMZN.csv')


#수정종가 데이터 슬라이싱
df['Adj Close'].plot(figsize=(16,9))


price_df=df.loc[:,['Adj Close']].copy()

price_df.plot(figsize=(16,9))


from_date ='1998-06-01'

to_date='2005-01-03'




plt.plot(df['Date'],df['Adj Close'],color='blue')



price_df.loc[from_date:to_date].plot(figsize=(16,9))



price=df['Date'].str.contains('1998|1999|2000|2001|2002|2003')
price_df=df[price]


price_df['Adj Close'].plot(figsize=(16,9))


price_df['daily_rtn']=price_df['Adj Close'].pct_change()



price_df.head(n=10)

price_df['st_rtn']=(1+price_df['daily_rtn']).cumprod()


price_df['st_rtn'].plot(figsize=(16,9))




df['daily_rtn']=df['Adj Close'].pct_change()

df['st_rtn']=(1+df['daily_rtn']).cumprod()


df['st_rtn'].plot(figsize=(16,9))



df.tail(n=10)

hm =df['Adj Close'].cummax()
da=df['Adj Close'] /hm -1.0


hdd=da.cummin()


hdd.plot(figsize=(16,9))


ca=df.loc['2019-06-24','st_rtn'] **(252./len(df.index))-1
