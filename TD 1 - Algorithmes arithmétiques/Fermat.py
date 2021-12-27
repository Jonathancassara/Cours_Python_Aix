#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 2 27/12/2021
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git

from random import randrange


def test_Fermat(n : int) -> bool:
    #generation de 'a' pour que : 1<a<n
    a = randrange(2,n-1)
    #application du petit theoreme de fermat a^x = a (mod x)
    resultat = (a ** (n - 1)) % n
    #si le résultat vaut 1, on peut rien conclure de façon sure.
    if resultat == 1:
        return True
    # si le résultat est différent de 1 alors n n'est pas Premier
    else:
        return False
