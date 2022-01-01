#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 1  01/01/2022
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git
#La suite de Syracuse

from typing import List


def syracuse(N : int) -> tuple[List[int], List[int]]:
    List = [N]
    if N == 1:
        return [1]
    elif N % 2 == 0:
        List.extend(syracuse(N/2))
    else:
        List.extend(syracuse(N*3+1))
    return List
