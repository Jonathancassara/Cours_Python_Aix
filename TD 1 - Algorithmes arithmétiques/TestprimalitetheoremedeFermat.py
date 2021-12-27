#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 1 18/12/2021
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git

import random
n = input("N")
k = input("K")
def test_Fermat(n : int, k : int) -> bool:
    a = random.randint(1,n-1)
    if (a ** (n - 1)) % n == 1 and k >= 1 and k < n:
        return True
    else:
        return False
    
def display_Fermat(n : int, k : int) -> None:
   test_Fermat(n, k)
   if test_Fermat(n, k) is True:
       print("premier")
   elif test_Fermat(n, k) is False:
       print("non premier")