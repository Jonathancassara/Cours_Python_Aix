#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Devoir 1 Agenda
# Auteur : Jonathan CASSARA-GOHIER
# Version 1.5 17/12/2021
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
            logging.info('L\'utilisateur a fait le choix 2.Chercher et Afficher')
            Nom = input("Qui recherchez-vous ? :")
            
            if Nom in file_name:
                csv_file = csv.reader(open(file_name, 'r'))
                for row in csv_file:
                    if Nom == row[1]:
                        #on affiche le ou les résultats de la ligne avec le Nom d'utilisateur
                        print(row)
            
                
                
            
                
                                        
            
            
            
        # 3.Ajouter un utilisateur  
        # je n'ai pas fait le choix de vérifier si le numéro avait bien 10 chiffres comme sur le systeme en France
        # car l'utilisateur peut ajouter un numéro étranger
        # ou vouloir mettre les indicatifs pays devant le numero par exemple 33602030405 ou un numero polonais (9 ou 11 chiffres) 48 500 500 500 48 12 000 000 000   
        elif selection == '3':
                logging.info('L\'utilisateur a fait le choix 3.Ajouter')
                Nom = input("Entrez Le Nom : ")
                Prenom = input("Entrez Le Prenom : ")
                #Vérifier si la personne existe déjà
                if Nom and Prenom in open(file_name).read() :
                    print("La personne est déjà présente")
                    logging.info('Ajout.la personne existe déjà')
                    modifier_Telephone = input("modifier le numéro ? [o/N] :")
                    modifier_Telephone = modifier_Telephone.strip().lower()
                    #Ajout du numéro de Téléphone
                    if modifier_Telephone.startswith('o'):
                            Telephone = input("Quelle est le numéro ? : ")
                            if Telephone.isdigit(): 
                            #Vérification si déjà présent
                                if Telephone in open(file_name).read() :
                                    print("le numéro existe déjà")
                                    logging.info('Ajout. la personne et le numéro existe déjà')
                                else:
                                    #Si numéro absent , on ajoute
                                    with open(file_name, 'a',newline='') as fichiercsv:
                                        writer=csv.writer(fichiercsv)
                                        writer.writerow([Nom.strip(), Prenom.strip(), Telephone])
                            else:
                                #si l'user tente d'inscrire des caractères autre que des chiffres         
                                print("Merci de saisir des chiffres uniquement")
                                logging.info('Ajout. la personne et le numéro existe déjà, mais tentative numéro non chiffre')
                    #Si l'user ne veut pas modifier le numéro on quitte            
                    elif modifier_Telephone.startswith('n') or modifier_Telephone == '':
                        print("Aucune modification faite")
                    else:
                        #l'user n'a pas répondu par oui ou non
                        print("Répondez par 'o' ou 'n'")        
                            
                else:
                    Telephone = input("Entrez Le Numéro de Téléphone : ")
                    # Vérification si l 'user entre bien que des chiffres pour le téléphone
                    if Telephone.isdigit(): 
                    #Vérification si déjà présent
                        if Telephone in open(file_name).read() :
                            print("le numéro existe déjà")
                            logging.info('Ajout. la personne n existe pas et le numéro existe déjà')
                            modifier_Telephone = input("modifier le numéro ? [o/N] :")
                            modifier_Telephone = modifier_Telephone.strip().lower()
                            #Ajout du numéro de Téléphone
                            if modifier_Telephone.startswith('o'):
                                Telephone = input("Quelle est le numéro ? : ")
                                with open(file_name, 'a',newline='') as fichiercsv:
                                    writer=csv.writer(fichiercsv)
                                    writer.writerow([Nom.strip(), Prenom.strip(), Telephone])
                                    logging.info('Ajout fait')
                            elif modifier_Telephone.startswith('n') or modifier_Telephone == '':
                                print("Aucune modification faite")
                            else:
                                print("Répondez par 'o' ou 'n'")
                        else:
                            with open(file_name, 'a',newline='') as fichiercsv:
                                writer=csv.writer(fichiercsv)
                                writer.writerow([Nom.strip(), Prenom.strip(), Telephone])
                    else:
                        #l'user tente de saisir un téléphone sans chiffre         
                        print("Merci de saisir des chiffres uniquement")
                
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
