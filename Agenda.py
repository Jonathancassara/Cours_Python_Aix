#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Devoir 1 Agenda
# Auteur : Jonathan CASSARA-GOHIER
# Version 0.1  17/11/2021
# copie et utilisation non autorisé

import logging
from datetime import datetime
import csv
from pathlib import Path


#Logging
#Filename Dest %/logfilename.log
#encoding UTF-8 (Latin EUROPE)
# datefmt Format Jours Mois Année , Heure Minute Seconde
logging.basicConfig(filename="logfilename.log", encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# Création et vérification du fichier CSV dans le répertoire
try:
    file = open('Agenda.csv')
    print("Fichier Agenda.csv est présent")
    file.close()
except FileNotFoundError:
    print("Fichier Absent")
    print("Création du Fichier Agenda.Csv")
    with open('Agenda.csv','w',newline='') as fichiercsv:
            writer=csv.writer(fichiercsv)
            writer.writerow(['Nom', 'Prénom', 'Téléphone'])
    exit
    
# Titre
print('------MENU AGENDA------')

# Menu de L'agenda
menu = {}
menu['1'] = "Importer un annuaire"
menu['2'] = "Chercher un utilisateur et afficher ses informations"
menu['3'] = "Ajouter un utilisateur"
menu['4'] = "Exporter l’annuaire"
menu['5'] = "Quitter"


while True:
    options = menu.keys()
    
    for entry in options:
        print (entry, menu[entry])
    selection = input("Merci de faire votre choix :")
    # 1.Importer un annuaire
    if selection == '1':
        print("Importer")
        logging.info('L\'utilisateur a fait le choix 1.Importer')
    # 2.Chercher un utilisateur et afficher ses informations
    elif selection == '2':
        print("Chercher et Afficher")
        logging.info('L\'utilisateur a fait le choix 2.Chercher et Afficher')
    # 3.Ajouter un utilisateur    
    elif selection == '3':
        print("Ajouter")
        logging.info('L\'utilisateur a fait le choix 3.Ajouter')  
    # 4.Exporter l’annuaire
    elif selection == '4':
        print("Expoter")
        logging.info('L\'utilisateur a fait le choix 4.Exporter')
    # 5.Quitter
    elif selection == '5':
        logging.info('L\'utilisateur a quitté l\'Agenda')
        break
    # Mauvais Choix
    else:
        print("Choix impossible!")
        logging.error('L\'utilisateur a fait un mauvais choix')