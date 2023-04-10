##
#@file: FinalTestr.py
#@version: 1.1
#@brief: Plot a figure with data from sensors and store it in a database
#@author: Manuel Estrada Maldonado
#@documentation: Manuel Estrada
#@date: 04/06/2023
#

#MODULES
from datetime import datetime
import matplotlib.pyplot as plt
import mysql.connector
import requests
import json

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="smability"
)
mycursor = mydb.cursor()

dataPM25I = []
timeStamp = []
dateTime = []

startDate=datetime(2023,4,4,00,00,00)
endDate=datetime(2023,4,5,00,00,00)



#Sensor Data
Ibero='2'
sensor = '7'
url = 'http://smability.sidtecmx.com/SmabilityAPI/GetData?'


#Query to request data

query = {'dtStart':startDate,'dtEnd':endDate,'token':Ibero,'idSensor':sensor}
response = requests.get(url, params=query)
y = json.dumps(response.json())#Change format response
alist= json.loads(y)

ReportQuery=f"INSERT INTO Report (ReportName,StartDate,EndDate,idUser) VALUES ('TestReport','{startDate}','{endDate}',1)"
mycursor.execute(ReportQuery)
#mydb.commit()


# Get resultset
mycursor.execute("SELECT * FROM  Report")
myresult = mycursor.fetchall()

print("Data from database: "+ mydb.database)
column_names = [i[0] for i in mycursor.description]

for x in column_names:
  print(x,end=" | ")
  
print("\n")

# Print resultset
for x in myresult:
  print(x)



for n in range(len(alist)):#Fill the first vector
    dataPM25I.append(float(alist[n]["Data"]))
    timeStamp.append(alist[n]["TimeStamp"])
    dateTime.append(datetime.strptime(timeStamp[n], "%Y-%m-%dT%H:%M:%S"))
    mycursor.execute(f"""INSERT INTO Sample (SampleNumber,TimeData,SampleData,idReport,idSensor,idMeasure)VALUES ({n},'{alist[n]["TimeStamp"]}',{alist[n]["Data"]},1,{Ibero},1)""")
mydb.commit()


#Plot data request
plt.figure(figsize=(16,9))
plt.plot(dateTime,dataPM25I, c="green", label='Ibero Ozone')
plt.title("OZONO ENERO-FEBRERO 2023", fontsize=25)
plt.grid()
plt.legend()
plt.savefig('ozono_traslape.png')#Generate a png file
plt.show()
plt.close()

# Cerrar el cursor y la conexión
mycursor.close()
mydb.close()

