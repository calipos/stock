# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 21:14:48 2020

@author: Administrator
"""

import requests
import time
import execjs
import matplotlib.pyplot as plt

def getUrl(fscode):
  head = 'http://fund.eastmoney.com/pingzhongdata/'
  tail = '.js?v='+ time.strftime("%Y%m%d%H%M%S",time.localtime())  
  return head+fscode+tail
print(getUrl('007818'))
def getWorth(fscode):
    #用requests获取到对应的文件
    content = requests.get(getUrl(fscode))
    
   #使用execjs获取到相应的数据
    jsContent = execjs.compile(content.text)
    print(jsContent)
    name = jsContent.eval('fS_name')
    code = jsContent.eval('fS_code')
    #单位净值走势
    netWorthTrend = jsContent.eval('Data_netWorthTrend')
    #累计净值走势
    ACWorthTrend = jsContent.eval('Data_ACWorthTrend')

    netWorth = []
    ACWorth = []

   #提取出里面的净值
    for dayWorth in netWorthTrend[::-1]:
        netWorth.append(dayWorth['y'])

    for dayACWorth in ACWorthTrend[::-1]:
        ACWorth.append(dayACWorth[1])
    print(name,code)
    return netWorth, ACWorth
wo
print(getWorth('688037'))

a=[1.2291, 1.2224, 1.2392, 1.1688, 1.1992, 1.2105, 1.2054, 1.2158, 1.2206, 1.1669, 1.2285, 1.2321, 1.2593, 1.2339, 1.1629, 1.1303, 1.1091, 1.1117, 1.0968, 1.0459, 1.0442, 1.052, 1.0377, 1.0379, 1.031, 1.016, 0.9962, 0.9813, 0.9797, 1.059, 1.1022, 1.0852, 1.0956, 1.0649, 1.0621, 1.0639, 1.0589, 1.0718, 1.0516, 1.0494, 1.0226, 1.042, 1.0367, 1.0297, 1.0249, 1.0063, 1, 0.9932, 1.005, 1.0041, 0.9915, 0.9783, 1.0048, 1.0232, 1.0283, 1.0279, 1.014, 0.997, 0.9918, 0.9871, 0.9894, 0.9772, 0.9768, 0.9671, 0.9512, 0.9547, 0.9467, 0.9411, 0.9394, 0.9399, 0.9295, 0.9286, 0.9467, 0.9518, 0.9507, 0.9594, 0.9429, 0.937, 0.9525, 0.9418, 0.9396, 0.9421, 0.9634, 0.9603, 0.9556, 0.9694, 0.9668, 0.9512, 0.9429, 0.9472, 0.955, 0.9714, 0.9509, 0.9409, 0.9449, 0.9509, 0.9386, 0.9439, 0.9535, 0.9522, 0.9599, 0.9837, 0.9717, 0.9748, 0.9557, 0.9471, 0.958, 0.9767, 0.966, 0.9949, 1.0127, 1.0041, 1.0048, 1.0035, 0.9842, 0.987, 1.0065, 1.0047, 0.999, 1.0061, 1.0144, 1.0029, 1.0014, 1]
b=[1.2291, 1.2224, 1.2392, 1.1688, 1.1992, 1.2105, 1.2054, 1.2158, 1.2206, 1.1669, 1.2285, 1.2321, 1.2593, 1.2339, 1.1629, 1.1303, 1.1091, 1.1117, 1.0968, 1.0459, 1.0442, 1.052, 1.0377, 1.0379, 1.031, 1.016, 0.9962, 0.9813, 0.9797, 1.059, 1.1022, 1.0852, 1.0956, 1.0649, 1.0621, 1.0639, 1.0589, 1.0718, 1.0516, 1.0494, 1.0226, 1.042, 1.0367, 1.0297, 1.0249, 1.0063, 1, 0.9932, 1.005, 1.0041, 0.9915, 0.9783, 1.0048, 1.0232, 1.0283, 1.0279, 1.014, 0.997, 0.9918, 0.9871, 0.9894, 0.9772, 0.9768, 0.9671, 0.9512, 0.9547, 0.9467, 0.9411, 0.9394, 0.9399, 0.9295, 0.9286, 0.9467, 0.9518, 0.9507, 0.9594, 0.9429, 0.937, 0.9525, 0.9418, 0.9396, 0.9421, 0.9634, 0.9603, 0.9556, 0.9694, 0.9668, 0.9512, 0.9429, 0.9472, 0.955, 0.9714, 0.9509, 0.9409, 0.9449, 0.9509, 0.9386, 0.9439, 0.9535, 0.9522, 0.9599, 0.9837, 0.9717, 0.9748, 0.9557, 0.9471, 0.958, 0.9767, 0.966, 0.9949, 1.0127, 1.0041, 1.0048, 1.0035, 0.9842, 0.987, 1.0065, 1.0047, 0.999, 1.0061, 1.0144, 1.0029, 1.0014, 1]
print(len(a))
print(a)
plt.figure(figsize=(10,5))
plt.plot(a[::-1])
plt.show()
def getAllCode():
    url = 'http://fund.eastmoney.com/js/fundcode_search.js'
    content = requests.get(url)
    jsContent = execjs.compile(content.text)
    rawData = jsContent.eval('r')
    allCode = []
    for code in rawData:
        allCode.append(code[0])
    return allCode
allCode = getAllCode()
print(len(allCode))