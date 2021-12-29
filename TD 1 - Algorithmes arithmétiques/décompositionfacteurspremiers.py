#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 2.1 28/12/2021
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git
#Décomposition en facteurs premiers

#def decompose(n :int) -> List[int]:
def dec(N):
    Resultat=[]
    d=2
    while N%d==0:
        Resultat.append(d)
        q=int(N/d)
        N=q
    d=3
    while d<=N:
        while N%d==0:
            Resultat.append(d)
            q=int(N/d)
            N=q
        d=d+2
    return Resultat