# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:36:26 2023

@author: JANTOGNELLI
"""
from math import gcd


def Sacados_glouton(elements, capacité):
    """
    Parameters
    ----------
    elements : list [[p,q],[p,q]]
        poids et quantité des éléments
    capacité : int
        capacité du sac à dos.

    Returns
    -------
    Liste,
    elements dans le sac
    """
    # On nettoie la liste
    nlist = []
    for i in range(len(elements)):
        if elements[i][1] != 0:
            nlist.append(elements[i])
    elements = nlist
    # On remplis le sac à dos
    sac = {}
    while capacité >= 0:
        # On cherche le plus grand PGCD entre un element et la capacité
        move = 0
        maxgcd = 0
        for j in range(len(elements)):
            if gcd(elements[j][0], capacité) > maxgcd and elements[j][0] <= capacité :
                maxgcd = gcd(elements[j][0],capacité)
                dgpcd = j
        sac[elements[dgpcd][0]] = 0
        while capacité > 0 or elements[dgpcd][1] > 0:
            if elements[dgpcd][0] <= capacité:
                move = 1
                capacité -= elements[dgpcd][0]
                elements[dgpcd][1] -= 1
                sac[elements[dgpcd][0]] += 1
            else:
                break
        elements.pop(dgpcd)
        if capacité == 0:
            return sac
        if move == 0:
            return sac, capacité
