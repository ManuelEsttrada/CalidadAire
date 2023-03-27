##
#@file: ozoneTest.py
#@version: 1.1
#@brief: Plot a figure and obtain an average ozone per day between two dates
#@author: Manuel Estrada Maldonado / using overlap from Jose 
#@documentation: Manuel Estrada
#@date: 02/21/2023
#



#MODULES
#from ctypes.wintypes import SIZE
from datetime import datetime
import matplotlib.pyplot as plt
import requests
import json

n=0
avg=0
samples=0
avg2=0
day=0

dataPM25I = []
timeStamp = []
dateTime = []
avgPerDay = []

#ID from sensor
Ibero='2'
sensor = '7'
url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?'

startDate=datetime(2023,1,1,00,00,00)
endDate=datetime(2023,2,27,00,00,00)
numDays = endDate.toordinal() - startDate.toordinal()+1

#Query to request data

query = {'dtStart':startDate,'dtEnd':endDate,'token':Ibero,'idSensor':sensor}
response = requests.get(url, params=query)
y = json.dumps(response.json())#Change format response
alist= json.loads(y)


for n in range(len(alist)):#Fill the first vector
    avg=avg+(float (alist[n]["Data"]))
    dataPM25I.append(float(alist[n]["Data"]))
    timeStamp.append(alist[n]["TimeStamp"])
    dateTime.append(datetime.strptime(timeStamp[n], "%Y-%m-%dT%H:%M:%S"))
    samples=samples+1
    if samples<290:
            avg2=avg2+(float(alist[n]["Data"]))        
    else:
            avg2=avg2/(samples)
            avgPerDay.append(avg2)
            day=day+1
            print("Day: ",day,": ",round(avg2,2))
            avg2=(float(alist[n]["Data"]))
            samples=0

avg=avg/len(dataPM25I)#Take data from sensor each five minutes

print("Total samples: ",len(dataPM25I))#iterates
print("Periodical average ozone: ",avg)#average
print("Period in days: ",numDays)

#Plot data request
plt.figure(figsize=(16,9))
plt.plot(dateTime,dataPM25I, c="green", label='Ibero Ozone')
plt.axhline(y=avg, color='r', linestyle='-',label='Average')
plt.title("OZONO ENERO-FEBRERO 2023", fontsize=25)
plt.grid()
plt.legend()
plt.savefig('ozono_traslape.png')#Generate a png file
plt.show()
plt.close()
