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

# Fermeture du script
def option0():
    print('\x1b[6;37;41m' + "Au Revoir" + '\x1b[0m')
    logging.info('REUSSI')
    
#Défintion pour le choix Importer un annuaire
def option1():
    # Demande à l'user le nom du fichier CSV à importer.
    importcsv = input("Quel est le nom de votre fichier annuaire ? " +'\x1b[6;37;41m' + " Uniquement au format CSV " + '\x1b[0m')
    # Création et vérification du fichier CSV dans le répertoire
    os.path.isfile(importcsv)
    file_extension = os.path.splitext(importcsv)[1]
    if file_extension.lower() == ".csv":
        try:    
            with open(importcsv , 'r') as file:
                logging.info('format de fichier correct')
                print("importation réussi")
        except IOError:
            # Si fichier absent et format correct, on demande si création du fichier
            print('\x1b[6;30;41m' + "Fichier Absent" + '\x1b[0m')
            answer = input('\x1b[0;30;44m' + "Voulez-vous créer le fichier ? oui ou non :" + '\x1b[0m').lower()
            if answer == 'oui':
                with open(importcsv, 'w', newline='') as importcsv:
                    writer = csv.writer(importcsv)
                    writer.writerow(['Nom', 'Prénom', 'Téléphone'])
                    print("Création réussi")
                    logging.info('création du fichier')
            # si le choix est non, on retourne au menu principal
            elif answer == 'non':
                print("Aucune Création de fichier")
                logging.info('aucun fichier créé retour au menu')
            return importcsv
    else:
        if file_extension.lower() != ".csv":
            logging.error('format de fichier incorrect')
            print('\x1b[6;30;41m' +"erreur de format de fichier" + '\x1b[0m')
        exit
