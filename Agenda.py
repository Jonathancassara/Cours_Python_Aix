#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Devoir 1 Agenda
# Auteur : Jonathan CASSARA-GOHIER
# Version 1.  22/11/2021
# copie et utilisation non autorisé
#
# Agenda.py
#

import logging
from datetime import datetime
import csv
from csv import reader
from pathlib import Path
import os
import random



# Logging
# Filename Dest %/logfilename.log
# encoding UTF-8 (Latin EUROPE)
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
menu['0'] = '\x1b[6;30;47m' + " Quitter " + '\x1b[0m'

# Définition des options


def options():
    for key in menu.keys():
        print(key, '--', menu[key])


# -------Menu Selection--------
while True:
        options = menu.keys()
        # Sélection menu
        for entry in options:
            print(entry, menu[entry])
        selection = input('\x1b[6;30;46m' + "Merci de faire votre choix :" + '\x1b[0m')
        # 1.Importer un annuaire
        if selection == '1':
            file_name = input("Quel est le nom de votre fichier annuaire ? " +'\x1b[6;37;41m' + " Uniquement au format CSV " + '\x1b[0m')
            os.path.isfile(file_name)
            file_extension = os.path.splitext(file_name)[1]
            if file_extension.lower() == ".csv":
                try:    
                    with open(file_name , 'r') as file:
                        logging.info('format de fichier correct')
                        print("importation réussi")
                except IOError:
                        print('\x1b[6;30;41m' + "Fichier Absent" + '\x1b[0m')
                        print('\x1b[0;30;44m' + "Création du Fichier" + file_name + '\x1b[0m')
                        with open(file_name,'w',newline='') as fichiercsv:
                            writer=csv.writer(fichiercsv)
                            writer.writerow(['Nom', 'Prénom', 'Téléphone'])
                            logging.info('création du fichier')
            else:
                if file_extension.lower() != ".csv":
                    logging.info('format de fichier incorrect')
                    print('\x1b[6;30;41m' + "erreur de format de fichier" + '\x1b[0m')
            
            logging.info('L\'utilisateur a fait le choix 1.Importer')
            
        # 2.Chercher un utilisateur et afficher ses informations
        elif selection == '2':
            def read_txt(file_name):
                file = open(file_name, "r")
                for row in file:
                    print(row)
                file.close()
            print(read_txt(file_name))
                                        
            logging.info('L\'utilisateur a fait le choix 2.Chercher et Afficher')
            
            
        # 3.Ajouter un utilisateur    
        elif selection == '3':
                Nom = input("Entrez Le Nom : ")
                Prenom = input("Entrez Le Prenom : ")
            # Vérification si l 'user entre bien que des chiffres pour le téléphone
                while True:
                    try:
                        Telephone = int(input("Entrez Le Numéro de Téléphone : "))
                        logging.info("Ajout d'un utilisateur")
                    except:
                        print("Merci de saisir des chiffres uniquement")
                        logging.info("Erreur dans la saisie de chiffres")
                    break  
                #Vérification si déjà présent
                while True:
                    try:
                        with open(file_name, 'a',newline='') as fichiercsv:
                            writer=csv.writer(fichiercsv)
                            writer.writerow([Nom, Prenom, int(Telephone)])
                            logging.info("Ajout fait")
                    except:
                        print("Le numéro exite déjà")
                        print("Voulez-vous le modifier ?")
                    break
                logging.info('L\'utilisateur a fait le choix 3.Ajouter')
        # 4.Exporter l’annuaire
        elif selection == '4':
            print("Expoter")
            logging.info('L\'utilisateur a fait le choix 4.Exporter')
            
        # 0.Quitter
        elif selection == '0':
            
            print('\x1b[6;37;41m' + "Au Revoir" + '\x1b[0m')
            logging.info('REUSSI')
            logging.info('L\'utilisateur a quitté l\'Agenda')
            break
        # Mauvais Choix
        else:
            print("Choix impossible! Merci de choisir un chiffre entre 0 et 4")
            logging.info('L\'utilisateur a fait un mauvais choix')
            break
