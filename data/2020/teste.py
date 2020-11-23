import mysql.connector
db = mysql.connector.connect(
	host="localhost",
	user="admin",
	passwd="ifsp@1234", 
	database="mapadevotos"
	)
    
print(mydb);