"""
Julien Antognelli
Advent of Code
Jour 1
"""
# On lit les données
data = open("données\jour1.txt")
data = data.readline()

def getfloor(data):
    res = 0
    for i in data:
        if i == "(":
            res += 1
        else:
            res -= 1
    return res

print(f"Partie 1:{getfloor(data)}")


def getbasement(data):
    floor = 0
    for i in range(len(data)):
        if data[i] == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return (i+1)
    return -1

print(f"partie 2: {getbasement(data)}")
