"""
julien Antognelli
Advent Of Code
jour 5
"""

data = open("données/jour5.txt").readlines()
for l in range(len(data)):
    data[l] = data[l].strip("\n")

def Partie1(data):
    res = 0
    forbiddenstr = ["ab", "cd", "pq", "xy"]
    for line in range(len(data)):
        vowelcount = 0
        doubleletter = False
        hasforbiddenstr = False
        for i in range(0,len(data[line])-1):
            if data[line][i] in "aeiou":
                vowelcount += 1
            if data[line][i] == data[line][i+1]:
                doubleletter = True
            if data[line][i] + data[line][i+1] in forbiddenstr:
                hasforbiddenstr = True
        if data[line][-1] in "aeiou":
            vowelcount += 1

        if vowelcount >= 3 and doubleletter is True and hasforbiddenstr is False:
            res += 1
    return res

print(f"partie 1: {Partie1(data)}")

# Partie 2

def Partie2(data):
    res = 0
    for line in range(len(data)):
        doublepair = False
        repeatingletter = False
        for i in range(len(data[line])-2):
            if data[line][i] == data[line][i+2]:
                repeatingletter = True
            if data[line][i]+data[line][i+1] in data[line][i+2:]:
                doublepair = True

        if doublepair is True and repeatingletter is True:
            res += 1
    return res

print(f"partie 2: {Partie2(data)}")