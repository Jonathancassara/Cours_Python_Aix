#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 1 18/12/2021
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git


import math
n = int(input("Votre chiffre : "))
def premier(n : int) -> bool:
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
        if d * d > n:
            return True
    return True

if premier(n) == True:
    print("Votre nombre "+ str(n) + " est premier")
else :
    print("votre nombre " + str(n)+ " n'est pas premier")
