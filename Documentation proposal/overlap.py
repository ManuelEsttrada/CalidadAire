##
#@file: overlap.py
#@version: 1.1
#@brief: Plot figures whit data from multiples id sensor
#@author: ---
#documentation: Manuel Estrada &
#@date: --/--/----
#

#MODULES
from ctypes.wintypes import SIZE
import matplotlib.pyplot as plt
import requests
import json
from datetime import datetime

#Define id from each sensor & API url
ibero2 = '349b1230277f1c67577e4f5bee6ba486'
ibero1 = '2'
sensor = '7'
url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?'

#Build a query to request data from the first sensor
query = {'dtStart':datetime(2023,1,1,3,00,00),'dtEnd':datetime(2023,2,20,3,00,00),'token':ibero1,'idSensor':sensor}
response = requests.get(url, params=query)

y = json.dumps(response.json())#Change format response
alist = json.loads(y)

#Build a query to request data from the second sensor
query = {'dtStart':datetime(2023,1,1,3,00,00),'dtEnd':datetime(2023,2,20,3,00,00),'token':ibero2,'idSensor':sensor}
response = requests.get(url, params=query)

y = json.dumps(response.json())#Change format response
blist = json.loads(y)

#Vectors manipulation
dataPM25I2 = []
timeStamp = []
dateTime1 = []
dataPM25I1 =[]
dateTime2 =[]

for n in range(len(alist)):#Fill the first vectors
    print(n)
    dataPM25I2.append(float(alist[n]["Data"]))

    timeStamp.append(alist[n]["TimeStamp"])
    dateTime1.append(datetime.strptime(timeStamp[n], "%Y-%m-%dT%H:%M:%S"))

for n in range(len(blist)):#Fill vectors to second sensor
    print(n)
    dataPM25I1.append(float(blist[n]["Data"]))
    timeStamp.append(blist[n]["TimeStamp"])
    dateTime2.append(datetime.strptime(timeStamp[n], "%Y-%m-%dT%H:%M:%S"))

#Plot data from all requests
plt.figure(figsize=(16,9))
plt.plot(dateTime1,dataPM25I2, c="red", label='Ibero')
plt.plot(dateTime2,dataPM25I1, c="blue", label='Prepa Ibero')
plt.title("Ozono durante la semana de contingencia", fontsize=25)
plt.grid()
plt.legend()
plt.savefig('ozono_traslape.png')#Generate a png file
plt.show()
