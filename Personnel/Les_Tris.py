# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:00:55 2022

@author: JANTOGNELLI

Les Différents tris
"""


def echange(liste, i, j):
    temp = liste[i]
    liste[i] = liste[j]
    liste[j] = temp


def minimum(liste, debut, fin):
    petit = liste[debut]
    indice = debut
    for i in range(debut+1, fin):
        if liste[i] < petit:
            petit = liste[i]
            indice = i
    return indice


def tri_bulle(listing):
    liste = listing
    bornes_max = len(liste)
    while bornes_max != 0:
        greatest = liste[0]
        for i in range(bornes_max):
            if greatest > liste[i]:
                echange(liste, i-1, i)
            else:
                greatest = liste[i]
        bornes_max -= 1
    return liste


def tri_selection(listing):
    liste = listing
    bornes_max = len(liste)
    while bornes_max != 0:
        indiceminimum = minimum(liste, 0, bornes_max)
        temp = liste[indiceminimum]
        liste.pop(indiceminimum)
        liste.append(temp)
        bornes_max -= 1
    return liste


def tri_shuffle(listing):
    liste = listing
    leng = len(liste)
    turn = True
    while turn:
        great = liste[0]
        turn = False
        for i in range(leng):
            if great > liste[i]:
                liste.pop(liste.index(great))
                liste.insert(i, great)
                turn = True
            else:
                great = liste[i]
        small = liste[leng-1]
        for i in range(leng-1, 0, -1):
            if small < liste[i]:
                liste.pop(liste.index(small))
                liste.insert(i-1, small)
                turn = True
            else:
                small = liste[i-1]
    return liste


def Tri_Rapide(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste[len(liste)//2]
    biglist = []
    smalllist = []
    for i in range(len(liste)):
        if liste[i] > pivot:
            biglist.append(liste[i])
        elif liste[i] < pivot:
            smalllist.append(liste[i])
    return Tri_Rapide(smalllist) + [pivot] + Tri_Rapide(biglist)


def Tri_insertion(liste):
    for i in range(1, len(liste)):
        v = i
        while v != 0:
            if liste[v] < liste[v-1]:
                echange(liste, v, v-1)
                v -= 1
            else:
                break
    return liste


def insertdecale(liste, i, val):
    avant = liste[i]
    liste[i] = val
    for j in range(i, len(liste)-1):
        apres = liste[j+1]
        liste[j+1] = avant
        avant = apres
    liste.append(avant)
    return liste
