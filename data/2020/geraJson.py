#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import mysql.connector
from datetime import datetime
import time
import json

fout = open('candidates.json', 'w')
databaseName = 'mapadevotos2020'
db = mysql.connector.connect(
	host="localhost",
	user="admin",
	passwd="ifsp@1234", 
	database=databaseName
	)

mycursor = db.cursor()

#Leitura das escolas
escolasArray = []
escolasDict = dict()
sql = "SELECT nomeEscola, numZona, numLocal, latitude, longitude FROM mapadevotos2020.escolas;"
mycursor.execute(sql)
escolas = mycursor.fetchall()
numTotalEscolas = mycursor.rowcount
print("Total de escolas = ", numTotalEscolas)
for escola in escolas:
	# print esc
	escola = {
		"nomeEscola": escola[0],
		"numZona" : escola[1],
		"numLocal" : escola[2],
		"latitude" : escola[3],
		"longitude" : escola[4]		
	}
	escolasArray.append(escola)
# Fim da leitura das escolas

sql = "SELECT DISTINCT nomeCandidato, numCandidato, descCargo FROM mapadevotos2020.boletimdeurna WHERE  boletimdeurna.nomeMunicipio = 'Campinas' ORDER BY nomeCandidato;"

mycursor.execute(sql)
data = mycursor.fetchall()
numTotalCandidatos = mycursor.rowcount
print ("Número total de candidatos:", numTotalCandidatos)
numCandidatosProcessados = 1
stringToSave="{"+"\n"
stringToSave = stringToSave + '"candidates":['
fout.write(stringToSave)
for row in data:
	# candidato = "candidato"+str(numCandidatosProcessados)
	# stringToSave='"'+candidato+'":{\n'
	# fout.write(stringToSave)
	nomeCandidato = row[0].strip("'")
	nomeCandidato = nomeCandidato.replace("'", "")
	print (nomeCandidato)
	numCandidato = row[1]
	descCargo = row[2]
	stringToSave='{"nomeCandidato"'+":"+'"'+nomeCandidato+'",'+"\n"
	fout.write(stringToSave)
	stringToSave='"numeroCandidato"'+":"+'"'+str(numCandidato)+'",'+"\n"
	fout.write(stringToSave)
	stringToSave='"DescCargo"'+":"+'"'+descCargo+'",'+"\n"
	fout.write(stringToSave)
	stringToSave = '"escolas":[\n'
	fout.write(stringToSave)
	numEscolasProcessadas = 1
	for escola in escolasArray:
		nomeEscola = escola["nomeEscola"]
		numZona = escola["numZona"]
		numLocal = escola["numLocal"]
		latitude = escola["latitude"]
		longitude = escola["longitude"]
		sql = "SELECT nomeCandidato, sum(quantidadeVotos) from mapadevotos2020.boletimdeurna where numZona="+str(numZona)+" AND numLocal="+str(numLocal)+" AND nomeCandidato='"+nomeCandidato+"' group by nomeCandidato;"
		mycursor.execute(sql)
		data2 = mycursor.fetchall()
		registrosLidos = mycursor.rowcount
		escola = "escola"+str(numEscolasProcessadas)
		print ("registros Lidos", registrosLidos)
		if registrosLidos == 1:
			quantidadeVotos = data2[0][1]
			quantidadeVotos = str(quantidadeVotos)
		else:
			if registrosLidos == 0:
				quantidadeVotos = 0
			else:
				print("Erro")
		# stringToSave = '"'+escola+'":'
		# fout.write(stringToSave)
		stringToSave='{"nome":'+'"'+nomeEscola+'",'+'"latitude":'+str(latitude)+','+'"longitude":'+str(longitude)+','+'"quantidadeVotos":'+str(quantidadeVotos)+'}'

		if(numEscolasProcessadas < numTotalEscolas):
			stringToSave = stringToSave + ',\n'
		else:
			stringToSave = stringToSave + '\n'

		fout.write(stringToSave)
		numEscolasProcessadas = numEscolasProcessadas + 1
		print ("Escola processada: ", numEscolasProcessadas)

	# 	if (numEscolasProcessadas == 3): break
	# if(numCandidatosProcessados == 3): break
	stringToSave = ']\n'
	fout.write(stringToSave)
	numCandidatosProcessados = numCandidatosProcessados + 1
	print ("Número de candidatos processados: ", numCandidatosProcessados)
	stringToSave='}'
	if(numCandidatosProcessados < numTotalCandidatos):
		stringToSave = stringToSave + ',\n'
	else:
		stringToSave = stringToSave + '\n'
	fout.write(stringToSave)
stringToSave='}'+"\n"+'}'
fout.write(stringToSave)