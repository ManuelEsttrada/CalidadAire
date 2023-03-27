import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="prueba"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM DatosPrueba WHERE dato>10")

# Get results
myresult = mycursor.fetchall()

print("Data from database: "+ mydb.database+"\n")
column_names = [i[0] for i in mycursor.description]

print(column_names[0]+" "+column_names[1])

# Print results
for x in myresult:
  print(x[0]," ",x[1])


