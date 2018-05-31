import re
import os, os.path

''' 
Este script coge los ficheros etiquetados a mano por Elena A. y hace un recuento de cada tipo de etiqueta por fichero. 
El resultado se escribe en el archivo cuentas.txt
'''

def count(text,basename):
	etiquetas = ["<persName","<persName type=\"_deity\">","<persName type=\"nickname\">","<persName type=\"_nickname_deity\">","<addName","<addName type=\"_legitimacy\">","<placeName","<placeName type=\"_facility\">","<placeName type=\"_mythological\">","<geogName","<geogName type=\"_mythological\">","<orgName","<orgName type=\"_collective\"","<roleName","<roleName type=\"honorific\">","<roleName type=\"_family\">","<name>"]
	for etiqueta in etiquetas:
		file=open(path_cuentas, 'a')
		match = re.findall(etiqueta, text)
		cuenta=basename+", "+etiqueta+", "+str(len(match))+"\n"
		print cuenta
		file.write(cuenta)
	file.close()

# rootdir should contain the path to the folder where subtitles files are located 
rootdir = 'C:\Users\Mara\Documents\GitHub\hismetag-corpus\manually_tagged\selected\selected_2000_Elena'
path_cuentas= 'C:\Users\Mara\Documents\GitHub\hismetag-corpus\other\cuentas.csv'
for root, _, files in os.walk(rootdir):
    for file in files:
		basename=os.path.basename(file)
		localpath = os.path.realpath(os.path.join(root,basename))
		file_object  = open(localpath, 'r')
		text= file_object.read()
		count(text,basename)
		file_object.close()