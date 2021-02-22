from datetime import datetime
from pandas_datareader import data as pdr
import pandas as pd
import xlrd

start=datetime(2008,1,20)

end=datetime(2020,12,30)


samsung=pdr.DataReader('000660.KS','yahoo',start,end)


#시가총액 100위
stock_code=["005930",
"000660",
"005935",
"051910",
"207940",
"068270",
"035420",
"006400",
"005380",
"035720",
"028260",
"051900",
"000270",
"091990",
"012330",
"005490",
"066570",
"036570",
"017670",
"105560",
"015760",
"096770",
"034730",
"055550",
"032830",
"003550",
"018260",
"009150",
"326030",
"090430",
"033780",
"251270",
"086790",
"011170",
"000810",
"018880",
"068760",
"010950",
"009540",
"009830",
"010130",
"316140",
"086280",
"034220",
"019170",
"024110",
"003670",
"030200",
"006800",
"097950",
"352820",
"021240",
"004020",
"032640",
"096530",
"034020",
"196170",
"035250",
"008930",
"000100",
"271560",
"028300",
"161390",
"006280",
"003490",
"285130",
"011200",
"002790",
"267250",
"010140",
"011780",
"071050",
"128940",
"011070",
"139480",
"180640",
"000720",
"000120",
"036490",
"029780",
"088980",
"004990",
"016360",
"247540",
"011790",
"336260",
"078930",
"293490",
"263750",
"026960",
"003410",
"005387",
"008770",
"012750",
"032500",
"005940",
"012510",
"005830",
"095700",
"112610"]

import FinanceDataReader as fdr



krx=fdr.StockListing('KRX')



stock_name=krx[['Symbol','Name']]



stock_name1=stock_name[stock_name['Symbol'].isin(stock_code)]

stock_name1=stock_name1.reset_index()


stock_name1=stock_name1.drop(['index'],axis=1)


price=[]


for i in range(len(stock_name1)):
    price.append(fdr.DataReader('{}'.format(stock_name1['Symbol'][i]),'2008-01-21','2020-12-30'))
    
    price[i].to_csv('{}.csv'.format(stock_name1['Name'][i]))


a=price[1].index

import os
import glob
import pandas as pd
import numpy as np
import datetime


files=glob.glob('C:/Users/user/Desktop/연구/시가총액100위/*.csv')

path = "C:/Users/user/Desktop/연구/시가총액100위"

file_list =os.listdir(path)

len(files)

kr_stock=[]

a=pd.read_csv('C:/Users/user/Desktop/연구/시가총액100위/삼성전자.csv')
a['Date'].startswith('2008')
a['Date'].str.contains('2008')[1]



for file in file_list:
    path = "C:/Users/user/Desktop/연구/시가총액100위"
    data=pd.read_csv(path+"/"+file)
    if data['Date'][0] <= '2009-01-01':
        kr_stock.append(data)
        data.to_csv('{}'.format(file))
    else:
        pass
        