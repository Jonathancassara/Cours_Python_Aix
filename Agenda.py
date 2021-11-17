#!/usr/bin/env python
# Devoir 1 Agenda
# Auteur : Jonathan CASSARA-GOHIER
# Version 0.1  17/11/2021

import logging
from datetime import datetime

#Logging
#Filename Dest %/logfilename.log
#encoding UTF-8 (Latin EUROPE)
# datefmt Format Jours Mois Année , Heure Minute Seconde
logging.basicConfig(filename="logfilename.log", encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

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
    if selection == '1':
        print("Importer")
        logging.info('L\'utilisateur a fait le choix 1.Importer')
    elif selection == '2':
        print("Chercher et Afficher")
        logging.info('L\'utilisateur a fait le choix 2.Chercher et Afficher')    
    elif selection == '3':
        print("Ajouter")
        logging.info('L\'utilisateur a fait le choix 3.Ajouter')  
    elif selection == '4':
        print("Expoter")
        logging.info('L\'utilisateur a fait le choix 4.Exporter')  
    elif selection == '5':
        logging.info('L\'utilisateur a quitté l\'Agenda')
        break
    else:
        print("Choix impossible!")
        logging.error('L\'utilisateur a fait un mauvais choix')