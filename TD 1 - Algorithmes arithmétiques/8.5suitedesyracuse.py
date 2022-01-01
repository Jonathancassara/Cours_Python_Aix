#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TD 1 - Algorithmes arithmétiques
# Auteur : Jonathan CASSARA-GOHIER
# Version 1  01/01/2022
# copie et utilisation non autorisé
# git@github.com:Jonathancassara/Cours_Python_Aix.git
#La suite de Syracuse

from typing import List, Sequence


def syracuse(N : int) -> tuple[List[int], List[int]]:
    Sequence[N]
    while Sequence[-1] != 1:
        if Sequence[-1] % 2 == 0:
            Sequence.append(Sequence[-1] // 2)
        else:
            Sequence.append(Sequence[-1] * 3 + 1)
    return print(syracuse(N))
