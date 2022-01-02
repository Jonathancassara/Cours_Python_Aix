#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 1  01/01/2022
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git
#Date du lendemain

Day = int(input("Entrez le jour:"))
Month = int(input("Entrez le mois:"))
Year = int(input("Entrez l'année:"))


if (Year % 4 == 0 and Year % 100 != 0) or Year % 400 ==0:
    bisextile=True
else:
    bisextile=False
if Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12:
    number_days = 31 
elif Month == 2 and bisextile():
    number_days = 29
elif Month == 2:
    number_days = 28
else:
    number_days = 30
if Day == number_days:
    Day = 1
    Month = Month + 1
else:
    Day = Day + 1
if Month == 13:
    Year = Year + 1
    Month = 1
print(Day, Month, Year)

#Date = input('Donnez une date au format Jour/Mois/Année JJ/MM/AAA: ')
#Day_parts = Date.slit('/')
#Date = Date.fromisoformat(f'{Day_parts[2]}-{Day_parts[1]}-{Day_parts[0]}')

#def demain(date : str) -> str:
#print(demain.strftime('%d/%m/%Y'))      