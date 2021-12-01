#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Devoir 1 Agenda
# Auteur : Jonathan CASSARA-GOHIER
# Version 1.  22/11/2021
# copie et utilisation non autorisé
#
# Menu.py
#

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



class Fichiercsv:
    #Défintion pour le choix Importer un annuaire
    def option1(fichier_csv):
        # Demande à l'user le nom du fichier CSV à importer.
        fichier_csv = input("Quel est le nom de votre fichier annuaire ? " +'\x1b[6;37;41m' + " Uniquement au format CSV " + '\x1b[0m')
        os.path.isfile(fichier_csv)
        file_extension = os.path.splitext(fichier_csv)[1]
        #Vérification de l'extention du fichier en .CSV
        if file_extension.lower() == ".csv":
            try:
                #si fichier présent et format correct alors création    
                with open(fichier_csv , 'r') as file:
                    logging.info('format de fichier correct')
                    print("importation réussi de :", fichier_csv)
                    return
            except IOError:
                    #Si fichier absent et format correct, on demande si création du fichier
                    print('\x1b[6;30;41m' + "Fichier Absent" + '\x1b[0m')
                    answer = input('\x1b[0;30;44m' + "Voulez-vous créer le fichier ? oui ou non :" + '\x1b[0m').lower()
                    if answer == 'oui':
                        with open(fichier_csv,'w',newline='') as fichier_csv:
                            writer=csv.writer(fichier_csv)
                            writer.writerow(['Nom', 'Prénom', 'Téléphone'])
                            print("Création réussi")
                            logging.info('création du fichier')
                    #si le choix est non, on retourne au menu principal
                    elif answer == 'non':
                        print("Aucune Création de fichier")
                        logging.info('aucun fichier créé retour au menu')
                    return fichier_csv            
        else:
            if file_extension.lower() != ".csv":
                logging.error('format de fichier incorrect')
                print('\x1b[6;30;41m' + "erreur de format de fichier" + '\x1b[0m')
        return fichier_csv



    #Défintion pour le choix Chercher un utilisateur et afficher ses informations
def option2():
    print(Fichiercsv)  
            
#Défintion pour le choix Ajouter un utilisateur
def option3():
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
