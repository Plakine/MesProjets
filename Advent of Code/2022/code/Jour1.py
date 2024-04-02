"""
Advent of Code.

jour 1
Partie 1 et 2
Somme , les trois plus grand
"""

file = open("..\\Data\\j1.txt", "r")
lines = [el.strip("\n") for el in file.readlines()]
i = 0
res = []
curres = 0
while i < len(lines):
    if lines[i] != "":
        curres += int(lines[i])
    else:
        res.append(curres)
        curres = 0
    i += 1
maxi = res[0]
for i in range(1, len(res)):
    if res[i] > maxi:
        maxi = res[i]
print(maxi)
# Partie 1 : fonction maximum


# Partie 2 : 3_meilleurs
i = 0
res = []
curres = 0
while i < len(lines):
    if lines[i] != "":
        curres += int(lines[i])
    else:
        res.append(curres)
        curres = 0
    i += 1
p1, p2, p3 = 0, 0, 0
for i in range(len(res)):
    if res[i] > p1:
        p3 = p2
        p2 = p1
        p1 = res[i]
    elif res[i] > p2:
        p3 = p2
        p2 = res[i]
    elif res[i] > p3:
        p3 = res[i]
print(p1+p2+p3)
