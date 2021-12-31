#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 1 31/12/2021
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git
#Calcul de la puissance d’un entier
#méthode optimisée

def pow_opt(x: int, n: int) -> int:
    if n % 2 == 0:
        a = (x**2)**(n/2)
        return print(a)
    else:
        a = x*x**(n-1)
        return  print(a)

