data = open("DATA\\jour4.txt")
data = data.readlines()
for i in range(len(data)):
    data[i] = data[i].strip("\n")


def partie1():
    somme = 0
    for ligne in data:
        s = 0
        i = 0
        while ligne[i] != ":":
            i += 1
        cleared_ligne = ligne[i+2:]
        numbers = cleared_ligne.split(" | ")
        winning_nums = numbers[1].split(" ")
        my_nums = numbers[0].split(" ")
        for num in my_nums:
            if num in winning_nums and num != "":
                s += 1
        if s > 0:
            somme += 2**(s-1)
    return somme


def partie2():
    somme = 0
    lignes = [1 for i in range(len(data))]
    for ligne in range(len(data)):
        i = 0
        while data[ligne][i] != ":":
            i += 1
        cleared_ligne = data[ligne][i+2:]
        numbers = cleared_ligne.split(" | ")
        winning_nums = numbers[1].split(" ")
        my_nums = numbers[0].split(" ")
        s = 0
        for num in my_nums:
            if num in winning_nums and num != "":
                s += 1
        for n in range(1, s+1):
            if ligne+n < len(lignes):
                lignes[ligne+n] = lignes[ligne+n] + (1*lignes[ligne])
        somme += lignes[ligne]
    return somme


print("Jour 4: \n  Partie 1:", (partie1()), "\n  Partie 2:", (partie2()))
