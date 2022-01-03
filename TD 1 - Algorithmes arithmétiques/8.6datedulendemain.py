#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 1  01/01/2022
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git
#Date du lendemain

#demande a l utilisateur d'entrer une date
today = input('Entrez une date au format JJ/MM/AAAA : ')

#découpage de la date d aujourd hui en jour mois annee
day, month, year = today.split('/')
#verification du format de la date
us_date_style = False
if us_date_style:
    day, month = month, day
day, month, year = int(day), int(month), int(year)

#verification si l'année est bisextile ou non
if not year % 400:
    bisextile = True
elif not year % 100:
    bisextile = False
elif not year % 4:
    bisextile = True
else:
    bisextile = False
    
tday, tmonth, tyear = day + 1, month, year

#verification si l annee est compris entre 1582 et 9999
if year < 1583 or year > 9999:
    print("Entrez une année comprise entre 1583 et 9999")
    exit()

#verification du nombre de jous de le mois ecrit par l utilisateutr exemple Janvier 31 jours; mars 31 jours etc 
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    max_day_value = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    max_day_value = 30
elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    max_day_value = 29
else:
    max_day_value = 28

#verification du nombre de mois ecrit par l'utilisateur
if month < 1 or month > 12:
    print("Merci d'entrer un mois correct")
    exit()
elif day < 1 or day > max_day_value:
    print("Merci d'entrer un jour correct")
    exit()
else:
    True
    
    
days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]
#verification si le mois de verifier a 28 ou 29 jours
if tday > days_per_month[month-1]:
    if month == 2 and bisextile and tday == 29:
        pass
    else:
        tday, tmonth = 1, month + 1

if tmonth == 13:
    
    tday, tmonth, tyear = 1, 1, year+1

date_tuple = (tmonth, tday, tyear) if us_date_style else (tday, tmonth, tyear)
tomorrow = '{:d}/{:d}/{:d}'.format(*date_tuple)
print('Aujourd\'hui, nous somme le  {:s}, demain, nous serons le {:s}.'.format(today, tomorrow))