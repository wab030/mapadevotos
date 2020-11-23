#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import mysql.connector
from datetime import datetime
import time

db = mysql.connector.connect(
	host="localhost",
	user="admin",
	passwd="ifsp@1234", 
	database="mapadevotos2020"
	)

mycursor = db.cursor()

# Function to delete tables
def dropTable(tabela):
	sql = "DROP TABLE "+tabela;
	mycursor.execute(sql);
	print ("Tabela "+tabela+" excluída.")
	return 0

def imprimeCampos(dataGer, horaGer, codPleito, codEleicao, estado, codCargo, descCargo, numZona, numSecao, numLocal, numPartido, nomePartido, codMunicipio, nomeMunicipio, numCandidato, nomeCandidato, quantidadeVotos):
	print("Data geração: ", dataGer)
	print("Hora da geração: ", horaGer)
	print("Código do pleito: ", codPleito)
	print("Código da eleição : ", codEleicao)
	print("Estado : ", estado)
	print("Código do cargo: ", codCargo)
	print("Descrição do cargo: ", descCargo)
	print("Número da zona: ", numZona)
	print("Número da seção: ", numSecao)
	print("Número do local: ", numLocal)
	print("Número do partido: ", numPartido)
	print("Nome do partido: ", nomePartido)
	print("Código do município: ", codMunicipio)
	print("Nome do município: ", nomeMunicipio)
	print("Número do candidato: ", numCandidato)
	print("Nome do candidato: ", nomeCandidato)

dropTable('boletimdeurna')

mycursor.execute("CREATE TABLE mapadevotos2020.boletimdeurna (idBu INT NOT NULL AUTO_INCREMENT, dataGer DATETIME NULL, horaGer DATETIME NULL, codPleito INT NULL, codEleicao INT NULL, estado VARCHAR(2) NULL, codCargo INT,descCargo VARCHAR(25), numZona INT, numSecao INT, numLocal INT, numPartido INT, nomePartido VARCHAR(58), codMunicipio VARCHAR(5), nomeMunicipio VARCHAR(35), numCandidato VARCHAR(10), nomeCandidato VARCHAR(40), quantidadeVotos INT, PRIMARY KEY (idBu));")

# mycursor.execute("CREATE TABLE mapadevotos.boletimdeurna (idBu INT NOT NULL AUTO_INCREMENT, dataGer DATETIME NULL, horaGer DATETIME NULL, codPleito INT NULL, codEleicao INT NULL, estado VARCHAR(2) NULL, codCargo INT, descCargo VARCHAR(25), idCandidato INT NOT NULL, quantidadeVotos INT,idLocal INT NOT NULL,idMunicipio INT NOT NULL, idPartido INT NOT NULL,PRIMARY KEY (idbu),CONSTRAINT idCandidato FOREIGN KEY (idCandidato) REFERENCES candidatos (idCandidato),CONSTRAINT idLocal FOREIGN KEY (idLocal) REFERENCES locais (idLocal),CONSTRAINT idMunicipio FOREIGN KEY (idMunicipio) REFERENCES municipios (idMunicipio),CONSTRAINT idPartido FOREIGN KEY (idPartido) REFERENCES partidos (idPartido));")


print("Tabela boletimdeurna criada.")

file = codecs.open('bweb_1t_SP_181120201549.csv', 'rb', encoding='latin-1')

i = 0

for line in file:
	i = i + 1
	line = line.strip()
	#print(line)
	#print('\n')
	if(i == 1): continue 
	campos = line.split(';')

	dataGer = campos[0].strip('"')
	dataGer = datetime.strptime(dataGer, '%d/%m/%Y')
	# print("Data da geração", dataGer)

	horaGer = campos[1].strip('"')
	# horaGer = horaGer.strftime("%H:%M:%S")
	horaGer = datetime.strptime(horaGer, '%H:%M:%S')
	# print("Hora da geração", horaGer)

	anoEleicao = campos[2].strip('"') 
	#print("Ano da eleição", anoEleicao)

	codTipoEleicao = campos[3].strip('"')
	#print(codTipoEleicao)

	numTipoEleicao = campos[4].strip('"')
	#print(numTipoEleicao)

	codPleito = campos[5].strip('"')
	#print("Código do Pleito", codPleito)

	dataPleito = campos[6].strip('"')
	dataPleito = datetime.strptime(dataPleito, '%d/%m/%Y')
	#print(dataPleito)

	numTurno = campos[7].strip('"')
	#print(numTurno)
	codEleicao = campos[8].strip('"')
	#print(codEleicao)
	descEleicao = campos[9].strip('"')
	#print(descEleicao)

	estado = campos[10].strip('"')
	#print("Estado ", estado)

	codMunicipio = campos[11].strip('"')
	#print("Código do município ", codMunicipio)
	nomeMunicipio = campos[12].strip('"')
	nomeMunicipio = nomeMunicipio.replace("'", "") #Removendo o caso de cidades como Pau d'alho que pode causar problemas ao gravar no mysql.
	#print("Nome do município ", nomeMunicipio)

	numZona = campos[13].strip('"')
	#print("Número da zona ", numZona)
	numSecao = campos[14].strip('"')
	#print("Número da seção ", numSecao)
	numLocal = campos[15].strip('"')
	#print("Número do local ", numLocal)

	codCargo = campos[16].strip('"')
	#print("Código do cargo ", codCargo)
	descCargo = campos[17].strip('"')
	#print("Descrição do cargo ", descCargo)

	numPartido = campos[18].strip('"')
	if(numPartido == '#NULO#'): numPartido = 100
	#print("Número do partido ", numPartido)
	siglaPartido = campos[19].strip('"') 
	if(siglaPartido == '#NULO#'): siglaPartido = ''
	#print("Sigla do partido ", siglaPartido)
	nomePartido = campos[20].strip('"')
	#print("Nome do partido ", nomePartido)

	dataBU = campos[21].strip('"')
	#print("Data do BU ", dataBU)
	quantidadeAptos = campos[22].strip('"')
	#print("Quantidade de eleitores aptos ", quantidadeAptos)
	quantidadeComparecimento = campos[23].strip('"')
	#print("Quantidade de comparecimento ", quantidadeComparecimento)
	quantidadeAbstencoes = campos[24].strip('"')
	#print("Quantidade de abstenções ", quantidadeAbstencoes)

	codTipoUrna = campos[25].strip('"')
	#print("Código tipo de urna ", codTipoUrna)
	descTipoUrna = campos[26].strip('"')
	#print("Descrição tipo de urna ", descTipoUrna)
	codTipoVotavel = campos[27].strip('"')
	#print("Código tipo votável ", codTipoVotavel)
	descTipoVotavel = campos[28].strip('"')
	#print("Descrição tipo votável ", descTipoVotavel)

	numCandidato = campos[29].strip('"')
	#print("Número do candidato ", numCandidato)
	nomeCandidato = campos[30].strip('"')
	#print("Nome do Candidato ", nomeCandidato)

	quantidadeVotos = campos[31].strip('"')
	# print("Quantidade de votos ", quantidadeVotos)

	numUrnaEfetivada = campos[32].strip('"')
	# print("Número urna efetivada ", numUrnaEfetivada)

	# imprimeCampos(dataGer, horaGer, codPleito, codEleicao, estado, codCargo, descCargo, numZona, numSecao, numLocal, numPartido, nomePartido, codMunicipio, nomeMunicipio, numCandidato, nomeCandidato, quantidadeVotos)

	sql = "INSERT INTO boletimdeurna (dataGer, horaGer, codPleito, codEleicao, estado, codCargo, descCargo, numZona, numSecao, numLocal, numPartido, nomePartido, codMunicipio, nomeMunicipio, numCandidato, nomeCandidato, quantidadeVotos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

	#val = (dataGer,horaGer, codPleito, codEleicao, estado, codCargo, descCargo, idCandidato , idLocal, idMunicipio , idPartido)
	val = (dataGer, horaGer, codPleito, codEleicao, estado, codCargo, descCargo, numZona, numSecao, numLocal, numPartido, nomePartido, codMunicipio, nomeMunicipio, numCandidato, nomeCandidato, quantidadeVotos)
	print(nomeMunicipio)
	if(nomeMunicipio == "CAMPINAS"): 
		
		mycursor.execute(sql, val)

	if(i % 1000 == 0 ):
		print(i,"linhas incluídas")
		db.commit()
		# break

db.commit()
file.close()
