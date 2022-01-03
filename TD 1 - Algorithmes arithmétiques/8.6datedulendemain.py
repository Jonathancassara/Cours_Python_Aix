#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 1  01/01/2022
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git
#Date du lendemain

us_date_style = False
days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]
today = input('Entrez une date au format JJ/MM/AAAA : ')

day, month, year = today.split('/')
if us_date_style:
    day, month = month, day
day, month, year = int(day), int(month), int(year)

if not year % 400:
    bisextile = True
elif not year % 100:
    bisextile = False
elif not year % 4:
    bisextile = True
else:
    bisextile = False
    
tday, tmonth, tyear = day + 1, month, year

if tday > days_per_month[month-1]:
    if month == 2 and bisextile and tday == 29:
        pass
    else:
        tday, tmonth = 1, month + 1

if tmonth == 13:
    # Yup: it must be 1 January of the next year
    tday, tmonth, tyear = 1, 1, year+1

date_tuple = (tmonth, tday, tyear) if us_date_style else (tday, tmonth, tyear)
tomorrow = '{:d}/{:d}/{:d}'.format(*date_tuple)
print('Aujourd\'hui, nous somme le  {:s}, demain, nous serons le {:s}.'.format(today, tomorrow))