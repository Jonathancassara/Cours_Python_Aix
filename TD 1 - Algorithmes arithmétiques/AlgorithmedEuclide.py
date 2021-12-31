#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 1 31/12/2021
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git
#Algorithme d’Euclide

def euclide (a: int, b : int, verbose: bool = False) -> int:
    
    a0, b0= a, b
    while True:
        r = a % b
        if r == 0:
            break
        else:
            a,b = b,r
            
    print('Le PGCD de', a0, 'et', b0, 'vaut', b,' le reste est de',r)
    print(a0 // b, 'x', b, '=', (a0 // b * b))
    print(b0 // b, 'x', b, '=', (b0 // b * b))
