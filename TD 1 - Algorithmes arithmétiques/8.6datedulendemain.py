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


def check_format(Day, Month, Year) -> bool:
    if Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12:
        max_day_value = 31
    elif Month == 4 or Month == 6 or Month == 9 or Month == 11:
        max_day_value = 30
    elif Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
        max_day_value = 29
    else:
        max_day_value = 28

    if Month < 1 or Month > 12:
        False
    elif Day < 1 or Day > max_day_value:
        False
    else:
        True

def bisextile(Year) ->bool:
    if (Year % 400 == 0) and (Year % 100 == 0):
    #if (Year % 4 == 0 and Year % 100 != 0) or Year % 400 == 0:
        True
    elif (Year % 4 == 0 ) and ( Year % 100 != 0):
        True
    else:
        False

def max_year(Year) ->bool:
    if Year < 1583 or Year > 9999:
        False
    else:
        True
