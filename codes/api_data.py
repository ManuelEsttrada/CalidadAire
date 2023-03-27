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
#url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?token=2&dtStart=2022-02-01%2006%3A00%3A00&dtEnd=2022-02-24%2018%3A00%3A00'
url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?'
query = {'dtStart':datetime(2022,2,1,00,00,00),'dtEnd':datetime(2022,2,28,00,00,00),'token':'2','idSensor':'1001'}
response = requests.get(url, params=query)

#parse data
y = json.dumps(response.json())
alist = json.loads(y)

print(y)