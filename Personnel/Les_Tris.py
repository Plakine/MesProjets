

def minindice(Liste: list, min=0) -> int:
    """
    Trouve le plus petit élement dans une liste et renvoi son indice
    """
    indice = min
    valeur = Liste[min]
    for i in range(min, len(Liste)):
        if valeur > Liste[i]:
            valeur = Liste[i]
            indice = i
    return indice


def triechange(Liste, i, j):
    temp = Liste[i]
    Liste[i] = Liste[j]
    Liste[j] = temp
    del temp


def triselection(Liste):
    fullist = len(Liste)
    for indice in range(fullist):
        triechange(Liste, minindice(Liste, indice), indice)
    return Liste


def tri_insertion(Liste):
    for i in range(len(Liste)):
        ind = i
        while Liste[ind] < Liste[ind-1] and ind > 0:
            triechange(Liste, ind, ind-1)
            ind -= 1
    return Liste