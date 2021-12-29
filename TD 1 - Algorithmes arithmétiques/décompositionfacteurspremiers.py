#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 2.1 28/12/2021
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git
#Décomposition en facteurs premiers

#def decompose(n :int) -> List[int]:
def diviseurs(n):
    Liste_div=[]
    for i in range(2,n+1):
        if n%i==0:
            Liste_div.append(i)
    return Liste_div

def premier(k):
    p=1
    for i in range(2,k):
        if k%i==0:
            p=0
    return p

def diviseurs_premiers(n):
    Liste_div_premiers=[]
    for i in diviseurs(n):
        if premier(i)==i:
            Liste_div_premiers.append(i)
    return Liste_div_premiers