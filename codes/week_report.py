#@file: week_report.py
#@brief: Get data from provider and plot related figures
#@author: ?????
#@date: **/**/****

#MODULES AND FRAMEWORKS
import requests
import json
import datetime
import matplotlib.pyplot as plt
from datetime import datetime
import collections

    #discard sets of 6:00 and 5:00pm!!! ////WHY????
    #API URL
    #idSensor
    #timeStamp

    #url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?token=2&idSensor=7&dtStart=2022-02-01%2006%3A00%3A00&dtEnd=2022-02-24%2018%3A00%3A00'
    #url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?token=2&dtStart=2022-02-01%2006%3A00%3A00&dtEnd=2022-02-24%2018%3A00%3A00'
    #response = requests.get(url=url)


url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?'
    #query = {'dtStart':datetime(2022,3,21,00,00,00),'dtEnd':datetime(2022,3,27,00,00,00),'token':'349b1230277f1c67577e4f5bee6ba486','idSensor':'12'}


query = {'dtStart':datetime(2022,3,21,00,00,00),'dtEnd':datetime(2022,3,27,00,00,00),'token':'2','idSensor':'12'}
response = requests.get(url, params=query)


    #parse data
y = json.dumps(response.json())
alist = json.loads(y)

dataPM25 = []
timeStamp = []
dateTime = []

for n in range(len(alist)):#Fill vectors
    print(n)
    dataPM25.append(float(alist[n]["Data"]))

    timeStamp.append(alist[n]["TimeStamp"])
    dateTime.append(datetime.strptime(timeStamp[n], "%Y-%m-%dT%H:%M:%S"))

plt.figure(figsize=(16,9))
plt.plot(dateTime,dataPM25)
plt.grid()

plt.savefig('temperatura_ibero2.png')
plt.show()
