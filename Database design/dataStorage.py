##
#@file: ozoneTest.py
#@version: 1.1
#@brief: Plot a figure and obtain an average ozone per day between two dates
#@author: Manuel Estrada Maldonado / using overlap from Jose 
#@documentation: Manuel Estrada
#@date: 03/15/2023
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
  database="prueba"
)
mycursor = mydb.cursor()

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
