import requests
import json
import datetime
import matplotlib.pyplot as plt
from datetime import datetime
import collections
#discard sets of 6:00 and 5:00pm!!!
#API URL
#idSensor
#timeStamp

#url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?token=2&idSensor=7&dtStart=2022-02-01%2006%3A00%3A00&dtEnd=2022-02-24%2018%3A00%3A00'
url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?token=2&dtStart=2022-02-01%2006%3A00%3A00&dtEnd=2022-02-24%2018%3A00%3A00'
response = requests.get(url=url)

#parse data
y = json.dumps(response.json())
alist = json.loads(y)

dataPM25 = []
timeStamp = []
dateTime = []

for n in range(len(alist)):
    print(n)
    dataPM25.append(float(alist[n]["Data"]))

    timeStamp.append(alist[n]["TimeStamp"])
    dateTime.append(datetime.strptime(timeStamp[n], "%Y-%m-%dT%H:%M:%S"))

plt.plot(dateTime,dataPM25)
plt.grid()
plt.show()
