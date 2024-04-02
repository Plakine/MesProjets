# -*- coding: utf-8 -*-
"""
Algorithme de Boyer Moore
Algorithme de recherche de sous-chaine
j'ai écrit ce programme à partir de ma lecture de l'article de recherche original
"""


def find_j(mot, j):
    plen = len(mot)-1
    k = j
    while k+plen-j > 0:
        if mot[j+1-min(0, k):] == mot[max(0 ,k):k+plen-j] and (k <= 0 or (mot[k-1] != mot[j])):
            return k+1
        k -= 1
    return False


def construire_table2(mot):
    f = False
    table2 = {len(mot)-1 : 1}
    for j in range(len(mot)-2, -1, -1):
        if not f:
            rpr = find_j(mot, j)
            if rpr is not False:
                table2[j] = len(mot) - rpr +1
            else:
                table2[j] = 2*len(mot)-(j+1)
            if rpr == 0 and rpr is not False:
                f = True
        else:
            table2[j] = table2[j+1] +1
    return table2


def pretraitement(mot, txtlen):
    motif = {}
    for letter in range(len(mot)-1):
        motif[mot[letter]] = len(mot)-(letter+1)
    motif[mot[len(mot)-1]] = 2 * txtlen
    return motif


def booyer_moore(txt, mot):
    if len(mot) > len(txt):
        return False
    i = len(mot)-1
    strlen = len(txt)
    motlen = len(mot)
    delta = pretraitement(mot, strlen)
    delta2 = construire_table2(mot)
    while True:
        while i <= strlen-1:
            if txt[i] in delta:
                i += delta[txt[i]]
            else:
                i += motlen
        if i < 2 * strlen:
            return False
        else:
            i = (i - 2*strlen) 
            j = motlen - 1
        while txt[i] == mot[j]:
            if  j == 0:
                return i
            i -= 1
            j -= 1
        if txt[i] in delta:
            if delta[txt[i]] == 2*strlen:
                i += max(0, delta2[j]) 
            else:
                i += max(delta[txt[i]], delta2[j])
        else:
            i += max(motlen, delta2[j])
