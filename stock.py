from jqdatasdk import *
import numpy
import csv
import os

dataFolder='dataFolder'
if(os.path.exists(dataFolder)):
    print("dataFolder already exist")
else:os.mkdir('./'+dataFolder)
     
authStatus = auth('15850798209','rbldevil198929aA')
print("sdk count = ",get_query_count())
all_securities=get_all_securities(['stock'])
all_securities.to_csv('stocklist.csv', sep=',')

print(all_securities[:2]) 
#df = get_price('603339.XSHG', start_date='2020-04-15', end_date='2020-04-17 23:00:00', frequency='minute') # 获得000001.XSHG的2015年01月的分钟数据, 只获取open+close字段
#print(df) 