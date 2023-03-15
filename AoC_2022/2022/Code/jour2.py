"""
Partie 1.

Consigne :
    Pierre feuille ciseau
    Calcul de points
"""
file = open("..\\Data\\j2.txt")
lines = [line.strip("\n") for line in file.readlines()]
p1 = []
p2 = []
score = 0
for element in lines:
    if element[0] == "A":
        p1.append(1)  # Pierre
    elif element[0] == "B":
        p1.append(2)  # Papier
    elif element[0] == "C":
        p1.append(3)  # Ciseaux
    if element[-1] == "X":
        p2.append(1)  # Pierre
        score += 1
    elif element[-1] == "Y":
        p2.append(2)  # Papier
        score += 2
    elif element[-1] == "Z":
        p2.append(3)  # Ciseaux
        score += 3
for i in range(len(p1)):
    if p1[i] == p2[i]:
        score += 3  # Nul
    if p2[i]-1 == p1[i] or p2[i]-1 == p1[i]-3:
        score += 6  # Victoire
    else:
        pass  # Défaite
print(score)
"""
Partie 2 :
Consigne
find the correct shape"""
p1 = []
p2 = []
score = 0
dicto = {"A": 1, "B": 2, "C": 3}
losdict = {1: 3, 2: 1, 3: 2}
windict = {1: 2, 2: 3, 3: 1}
for element in lines:
    p1.append(dicto[element[0]])
    p2.append(element[-1])
for i in range(len(p1)):
    if p2[i] == "Y":
        score += p1[i]
        score += 3
    elif p2[i] == "X":
        score += losdict[p1[i]]
    elif p2[i] == "Z":
        score += 6
        score += windict[p1[i]]

print(score)
