#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 1 28/12/2021
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git
# Crible d’Ératosthène

def eratosthene(n :int) -> bool:
    if n == 1:
        return False
    d = 2
    while d*d<= n:
        if n % d == 0:
            return False
        d += 1
    return True