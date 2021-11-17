#!/usr/bin/env python
# Devoir 1 Agenda
# Auteur : Jonathan CASSARA-GOHIER
# Version 0.1  17/11/2021

print('AGENDA')

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
    elif selection == '2':
            print("Chercher et Afficher")
    elif selection == '3':
        print("Ajouter")
    elif selection == '4':
        print("Expoter")
    elif selection == '5':
        break
    else:
        print("Choix impossible!")