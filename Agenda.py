#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Devoir 1 Agenda
# Auteur : Jonathan CASSARA-GOHIER
# Version 0.3  21/11/2021
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

# Création et vérification du fichier CSV dans le répertoire
try:
    with open('Agenda.csv','r') as file:
        print('\x1b[6;30;42m' + "Fichier Agenda.csv est présent" + '\x1b[0m')
except IOError:
    print('\x1b[6;30;41m' + "Fichier Absent" + '\x1b[0m')
    print('\x1b[0;30;44m' + "Création du Fichier Agenda.Csv" + '\x1b[0m')
    with open('Agenda.csv','w',newline='') as fichiercsv:
            writer=csv.writer(fichiercsv)
            writer.writerow(['Nom', 'Prénom', 'Téléphone'])
            writer.writerow(['Doe', 'John', '0000000000'])
    exit
    
# Titre
print('\x1b[6;30;47m' + '------MENU AGENDA------' + '\x1b[0m')

# Menu de L'agenda
menu = {}
menu['1'] = '\x1b[6;30;47m' + " Importer un annuaire " + '\x1b[0m'
menu['2'] = '\x1b[6;30;47m' + " Chercher un utilisateur et afficher ses informations " + '\x1b[0m'
menu['3'] = '\x1b[6;30;47m' + " Ajouter un utilisateur " + '\x1b[0m'
menu['4'] = '\x1b[6;30;47m' + " Exporter l’annuaire " + '\x1b[0m'
menu['5'] = '\x1b[6;30;47m' + " Quitter " + '\x1b[0m'

#Définition des options
def options():
    for key in menu.keys():
        print (key, '--', menu[key] )
        
#Défintion pour le choix Importer un annuaire
def option1():
    # Demande à l'user le nom du fichier CSV à importer.
    importation = input("Quel est le nom de votre fichier annuaire ? " +'\x1b[6;37;41m' + " Uniquement au format CSV " + '\x1b[0m')
    os.path.isfile(importation)
    file_extension = os.path.splitext(importation)[1]
    if file_extension.lower() == ".csv":
        try:    
            with open(importation , 'r') as file:
                logging.info('format de fichier correct')
                print("importation réussi")
        except IOError:
                print('\x1b[6;30;41m' + "Fichier Absent" + '\x1b[0m')
                print('\x1b[0;30;44m' + "Création du Fichier" + importation + '\x1b[0m')
                with open(importation,'w',newline='') as fichiercsv:
                    writer=csv.writer(fichiercsv)
                    writer.writerow(['Nom', 'Prénom', 'Téléphone'])
    else:
        if file_extension.lower() != ".csv":
            logging.error('format de fichier incorrect')
            print('\x1b[6;30;41m' + "erreur de format de fichier" + '\x1b[0m')
        
        

#Défintion pour le choix Chercher un utilisateur et afficher ses informations
def option2(importation = 'Agenda.csv'):
    with open(importation , 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            print('\x1b[6;30;42m' + row[1],'\x1b[6;30;42m' +  row[2],'\x1b[6;30;42m' +  row[3]+ '\x1b[0m')
            logging.info('Affichage des données')
            
#Défintion pour le choix Ajouter un utilisateur
def option3(importation = 'Agenda.csv'):
        Nom = input("Entrez Le Nom : ")
        Prenom = input("Entrez Le Prenom : ")
        # Vérification si l 'user entre bien que des chiffres pour le téléphone
        while True:
            try:
                Telephone = int(input("Entrez Le Numéro de Téléphone : "))
                logging.info("Ajout d'un utilisateur")
            except:
                print("Merci de saisir des chiffres uniquement")
            break  
        with open(importation, 'a',newline='') as fichiercsv:
                writer=csv.writer(fichiercsv)
                writer.writerow([Nom, Prenom, int(Telephone)])    
        
            

#Défintion pour le choix Exporter l’annuaire
def option4():
    print('\x1b[6;37;41m' + "REUSSI" + '\x1b[0m')
    logging.info('REUSSI')

#Fermeture du script avec suppression du fichier Agenda.csv
def option5():
    print('\x1b[6;37;41m' + "Suppression Agenda.csv" + '\x1b[0m')
    if os.path.exists('Agenda.csv'):
        os.remove('Agenda.csv')
        logging.info('suppression réussi du fichier Agenda.csv')
    else:
        print("Impossible de supprimer le fichier car il n'existe pas")
        logging.ERROR("Impossible de supprimer le fichier car il n'existe pas")


if __name__=='__main__':
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
        

    