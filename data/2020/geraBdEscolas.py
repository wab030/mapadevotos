#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	user="admin",
	passwd="ifsp@1234", 
	database="mapadevotos2020"
)

mycursor = db.cursor()

# Function to delete tables
def dropTable(tabela):
	sql = "DROP TABLE "+tabela
	mycursor.execute(sql)
	print("Tabela excluída "+tabela)
	return 0

#dropTable('escolas')

mycursor.execute("CREATE TABLE mapadevotos2020.escolas (idEscola INT AUTO_INCREMENT PRIMARY KEY, numZona INT, numLocal INT, nomeEscola VARCHAR(100), latitude FLOAT, longitude FLOAT)")
print("Tabela escolas criada.")

file = codecs.open('escolas.txt', 'rb', encoding='utf-8')

i = 0
for line in file:
	if (i == 0): 
		i = 1
		continue
	line = line.strip()
	campos = line.split(',')

	numZona = int(campos[0].strip('"'))
	numLocal = int(campos[1].strip('"'))
	nomeEscola = campos[2].strip("'")
	latitude = float(campos[3].strip('"'))
	longitude = float(campos[4].strip('"'))

	print(numZona, numLocal, nomeEscola, latitude, longitude)
	sql = "INSERT INTO escolas (numZona, numLocal, nomeEscola, latitude, longitude) VALUES (%s, %s, %s, %s, %s)"
	val = (numZona, numLocal, nomeEscola, latitude, longitude)
	mycursor.execute(sql, val)
	idLocal = mycursor.lastrowid
	print("Escola ",nomeEscola, "incluída no banco de dados. ")

	# sql = "SELECT * FROM partidos WHERE numPartido="+numPartido;
	# mycursor.execute(sql)
	# myresult = mycursor.fetchall()
	# print myresult
	# if(myresult):
	# 	for x in myresult:
	# 		print("Partido Cadastrado")
	#  			print(x)
 	#  	else:
 	#  		print "Partido não cadastrado"


db.commit()
file.close()