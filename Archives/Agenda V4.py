import csv
import os
from csv import reader
from pathlib import Path


# Création et vérification du fichier CSV dans le répertoire
try:
    with open('Agenda2.csv','r') as file:
        print('\x1b[6;30;42m' + "Fichier Agenda.csv est présent" + '\x1b[0m')
except IOError:
    print('\x1b[6;30;41m' + "Fichier Absent" + '\x1b[0m')
    print('\x1b[0;30;44m' + "Création du Fichier Agenda.Csv" + '\x1b[0m')
    with open('Agenda.csv','w',newline='') as fichiercsv:
            writer=csv.writer(fichiercsv)
            writer.writerow(['Nom', 'Prénom', 'Téléphone'])
            writer.writerow(['Doe', 'John', '0000000000'])
    exit
print("phone book:")
if os.path.isfile('Agenda.csv') == True:  
    csv_file=open('Agenda.csv','r')
    for row in csv_file:
        print(row)
    csv_file.close()
else:
    print ("Phone book file not created. First create it to read it")