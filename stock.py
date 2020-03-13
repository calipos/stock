# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:05:54 2020
@author: Administrator
"""
import pandas_datareader.data as web
import numpy as np 
import matplotlib.pyplot as plt 
import datetime
import yfinance  as yf
yf.pdr_override()
start = datetime.datetime(2020,1,1)#获取数据的时间段-起始时间
end = datetime.datetime(2020,3,1)#获取数据的时间段-结束时间
stock = web.get_data_yahoo("600797.SS",   start, end)#获取浙大网新2017年1月1日至今的股
 
stock['Adj Close'].plot(legend=True, figsize=(10,4))
plt.show()
stock.to_csv(r'table.csv',columns=stock.columns,index=True)