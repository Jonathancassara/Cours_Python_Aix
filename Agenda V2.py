#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Devoir 1 Agenda
# Auteur : Jonathan CASSARA-GOHIER
# Version 1.  22/11/2021
# copie et utilisation non autorisé

import logging
from datetime import datetime
import csv
from csv import reader
from pathlib import Path
import os
import random

#Logging
#Filename Dest %/logfilename.log
#encoding UTF-8 (Latin EUROPE)
# datefmt Format Jours Mois Année , Heure Minute Seconde
logging.basicConfig(filename="logfilename.log", encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# Titre
print('\x1b[6;30;47m' + '------MENU AGENDA------' + '\x1b[0m')

# Menu de L'agenda
menu = {}
menu['1'] = '\x1b[6;30;47m' + " Importer un annuaire " + '\x1b[0m'
menu['2'] = '\x1b[6;30;47m' + " Chercher un utilisateur et afficher ses informations " + '\x1b[0m'
menu['3'] = '\x1b[6;30;47m' + " Ajouter un utilisateur " + '\x1b[0m'
menu['4'] = '\x1b[6;30;47m' + " Exporter l’annuaire " + '\x1b[0m'
menu['5'] = '\x1b[6;30;47m' + " Quitter " + '\x1b[0m'

      

while True:
        options = menu.keys()
        #Sélection menu
        for entry in options:
            print (entry, menu[entry])
        selection = input('\x1b[6;30;46m' + "Merci de faire votre choix :" + '\x1b[0m')
        # 1.Importer un annuaire
        if selection == '1':
            option1()
            logging.info('L\'utilisateur a fait le choix 1.Importer')
        # 2.Chercher un utilisateur et afficher ses informations
        elif selection == '2':
            option2()
            print("Chercher et Afficher")
            logging.info('L\'utilisateur a fait le choix 2.Chercher et Afficher')
        # 3.Ajouter un utilisateur    
        elif selection == '3':
            option3()
            print("Ajouter")
            logging.info('L\'utilisateur a fait le choix 3.Ajouter')  
        # 4.Exporter l’annuaire
        elif selection == '4':
            option4()
            print("Expoter")
            logging.info('L\'utilisateur a fait le choix 4.Exporter')
        # 5.Quitter
        elif selection == '5':
            logging.info('L\'utilisateur a quitté l\'Agenda')
            option5()
            break
        # Mauvais Choix
        else:
            print("Choix impossible! Merci de choisir un chiffre entre 1 et 5.0")
            logging.error('L\'utilisateur a fait un mauvais choix')
        
#Définition des options
def options():
    for key in menu.keys():
        print (key, '--', menu[key] )

#Défintion pour le choix Importer un annuaire
def option1():
    print('\x1b[6;37;41m' + "REUSSI" + '\x1b[0m')
    logging.info('REUSSI')
        
        

#Défintion pour le choix Chercher un utilisateur et afficher ses informations
def option2(importation = 'Agenda.csv'):
    print('\x1b[6;37;41m' + "REUSSI" + '\x1b[0m')
    logging.info('REUSSI')
            
#Défintion pour le choix Ajouter un utilisateur
def option3(importation = 'Agenda.csv'):
    print('\x1b[6;37;41m' + "REUSSI" + '\x1b[0m')
    logging.info('REUSSI')    
            
        
            

#Défintion pour le choix Exporter l’annuaire
def option4():
    print('\x1b[6;37;41m' + "REUSSI" + '\x1b[0m')
    logging.info('REUSSI')
#Fermeture du script avec suppression du fichier Agenda.csv
def option5():
    print('\x1b[6;37;41m' + "REUSSI" + '\x1b[0m')
    logging.info('REUSSI')
