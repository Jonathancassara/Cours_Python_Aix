#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 2 29/12/2021
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git
#Décomposition en facteurs premiers

#def decompose(n :int) -> List[int]:
from typing import List


def decompose(n :int) -> List[int]:
    Resultat=[]
    d=2
    while n%d==0:
        Resultat.append(d)
        q=int(n/d)
        n=q
    d=3
    while d<=n:
        while n%d==0:
            Resultat.append(d)
            q=int(n/d)
            n=q
        d=d+2
    return Resultat