from jqdatasdk import *
import numpy
import csv
import os
import time
import datetime
import pandas as pd
import json
import string
import easyquotation


dataFolder='dataFolder'
if(os.path.exists(dataFolder)):
    print("dataFolder already exist")
else:os.mkdir('./'+dataFolder)


potentialList={}  
potentialRate=[-0.025,-0.019]

quotation = easyquotation.use('sina')
snapshot = quotation.market_snapshot(prefix=True)
codes = snapshot.keys()
print("there are "+str(len(codes))+"stocks.")
for code in codes:
    theName = snapshot[code]['name']
    if theName.find('ST')>=0:
        continue
    lastDayClose = snapshot[code]['close']
    currentDayHigh = snapshot[code]['high']
    currentDayLow = snapshot[code]['low']
    currentDayTurnover = snapshot[code]['turnover']
    if currentDayTurnover<1e5:
        continue
    currentDayVolume = snapshot[code]['volume']
    currentDayAvg = currentDayVolume/currentDayTurnover
    if currentDayAvg<lastDayClose:
        codeHead = code[:2]
        codeNum = code[2:]
        if codeNum[:3]=='300':
            continue
        if codeNum[:3]=='200':
            continue
        if codeNum[:3]=='900':
            continue
        if codeNum[:3]=='002':
            continue
        if codeNum[:3]=='730':
            continue
        if codeNum[:3]=='700':
            continue 
        if codeNum[:3]=='080':
            continue 
        if codeNum[:3]=='580':
            continue 
        if codeNum[:3]=='031':
            continue 
        if codeNum[:3]=='400':
            continue 
        theRate = (currentDayAvg-lastDayClose)/lastDayClose
        if theRate>potentialRate[0] and theRate<potentialRate[1]:
            if codeHead=='sh':
                potentialList[codeNum+'.XSHG']=theRate
            if codeHead=='sz':
                potentialList[codeNum+'.XSHE']=theRate
potentialList=sorted(potentialList.items(),key=lambda kv:(kv[1], kv[0]),reverse=False)
#print(potentialList)
print ('there are %d potential stocks.'%len(potentialList))
     
#authStatus = auth('15850798209','rbldevil198929aA')
#authStatus = auth('13308189942','rbldevil198929aA')
#authStatus = auth('15730085953','rbldevil198929aA')
authStatus = auth('18081550388','rbldevil198929aA')
print("sdk count = ",get_query_count())

#all_securities=get_all_securities(['stock'])
#all_securities.to_csv('stocklist.csv', sep=',')
all_securities=pd.read_csv('stocklist.csv', sep=',',index_col=[0])

targetCodeId=[]
all_securities_list=[]
for codeId in range(all_securities.index.size):
    all_securities_list.append(all_securities.index[codeId])
for code in potentialList:
    if code[0] in all_securities_list:
        codeId = all_securities_list.index(code[0])
        #print(codeId)
        targetCodeId.append(codeId)
        #print(code[0]+' : '+all_securities.index[codeId])

endDate='' 
nextStartDate=''
if time.localtime().tm_hour<16:
    endDate=str(datetime.date.today() -datetime.timedelta(days=1))
    nextStartDate=str(datetime.date.today())    
else:
    endDate=time.strftime('%Y-%m-%d',time.localtime())
    nextStartDate=str(datetime.date.today()+datetime.timedelta(days=1))
print(endDate)
currentEndDate_year = int(endDate.split('-')[0])
currentEndDate_month = int(endDate.split('-')[1])
currentEndDate_day =  int(endDate.split('-')[2])

#for codeId in range(all_securities.index.size):
for codeId in targetCodeId:  
    thisCode = all_securities.index[codeId]
    info_doc_path=(dataFolder+'/'+str(thisCode)+'_info.json')
    currentStartDate=''
    if(os.path.exists(info_doc_path)):
        infoDict={}
        with open(info_doc_path,'r') as load_f:infoDict = json.load(load_f)
        currentStartDate = infoDict['currentStartDate']
    else:
        currentStartDate = str(all_securities.start_date[codeId]).split(' ')[0]
        theBeginYear = int(currentStartDate.split('-')[0])
        theBeginMonth = int(currentStartDate.split('-')[1])
        theBeginDay = int(currentStartDate.split('-')[2])
        if currentEndDate_year*12+currentEndDate_month-theBeginYear*12+theBeginMonth>=24:
            currentStartDate = str(datetime.date.today() -datetime.timedelta(days=500))
        infoDict={'currentStartDate':currentStartDate};
        with open(info_doc_path,"w") as f: json.dump(infoDict,f)
    print("start date = ",currentStartDate)
    currentStartDate_year =int(currentStartDate.split('-')[0])
    currentStartDate_month = int(currentStartDate.split('-')[1])
    currentStartDate_day = int(currentStartDate.split('-')[2])
    
    if  currentStartDate_year*375+31*currentStartDate_month+currentStartDate_day>\
        currentEndDate_year*375+31*currentEndDate_month+currentEndDate_day:
        #print("StartDate : "+currentStartDate)
        #print("endDate : "+endDate)
        #print("date err")
        continue
    if currentEndDate_year==currentStartDate_year and currentEndDate_month==currentStartDate_month and currentEndDate_day==currentStartDate_day:
        print("the same date not need updata")
        continue
    else:
        df_add = get_price(thisCode, start_date=currentStartDate, end_date=endDate+' 23:00:00', frequency='minute') 
        df_add.to_csv(dataFolder+'/'+str(thisCode)+'.csv', sep=',', mode='a', header=False)
        infoDict={'currentStartDate':nextStartDate};
        with open(info_doc_path,"w") as f: json.dump(infoDict,f)
     

