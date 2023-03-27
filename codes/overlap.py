#@file: overlap.py
#@brief: Plot data from two or more id sensor
#@author: ?????
#@date: **/**/****


#MODULES
from ctypes.wintypes import SIZE
import matplotlib.pyplot as plt
import requests
import json
from datetime import datetime
ibero2 = '349b1230277f1c67577e4f5bee6ba486'
ibero1 = '2'
sensor = '7'

url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?'# API URL
query = {'dtStart':datetime(2022,5,9,3,00,00),'dtEnd':datetime(2022,5,10,3,00,00),'token':ibero1,'idSensor':sensor}
response = requests.get(url, params=query)#GET RESPONSE 

y = json.dumps(response.json())
alist = json.loads(y)#CAHNGE RESPONSE FORMAT

query = {'dtStart':datetime(2022,5,9,3,00,00),'dtEnd':datetime(2022,5,10,3,00,00),'token':ibero2,'idSensor':sensor}#SECOND QUERY
response = requests.get(url, params=query)

y = json.dumps(response.json())
blist = json.loads(y)

dataPM25I2 = []
timeStamp = []
dateTime1 = []
dataPM25I1 =[]
dateTime2 =[]

for n in range(len(alist)):#FILL VECTORS
    print(n)
    dataPM25I2.append(float(alist[n]["Data"]))

    timeStamp.append(alist[n]["TimeStamp"])
    dateTime1.append(datetime.strptime(timeStamp[n], "%Y-%m-%dT%H:%M:%S"))

for n in range(len(blist)):
    print(n)
    dataPM25I1.append(float(blist[n]["Data"]))
    timeStamp.append(blist[n]["TimeStamp"])
    dateTime2.append(datetime.strptime(timeStamp[n], "%Y-%m-%dT%H:%M:%S"))


#PLOT
plt.figure(figsize=(16,9))
plt.plot(dateTime1,dataPM25I2, c="red", label='Ibero')
plt.plot(dateTime2,dataPM25I1, c="blue", label='Prepa Ibero')
plt.title("Ozono durante la semana de contingencia", fontsize=25)
plt.grid()
plt.legend()
plt.savefig('ozono_traslape.png')
plt.show()
