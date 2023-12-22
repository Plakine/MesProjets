from functools import cache
data = open("data/jour12.txt").read().splitlines()
@cache
def solve(ligne, liste):
    res = 0
    if len(liste) == 0:
        if "#" not in ligne:
            return 1
        else:
            return 0
    if len(ligne) == 0:
        return 0
    if ligne[0] == ".":
        res = solve(ligne[1:], liste)
    elif ligne[0] == "#":
        res = group_test(ligne, liste)
    elif ligne[0] == "?":
        res = solve(ligne[1:], liste) + group_test(ligne, liste)
    return res


def group_test(liste, group):
    expected = group[0]
    pratique = liste[:expected].replace("?", "#")
    if pratique!= "#"*expected:
        return 0
    else:
        if len(liste) == expected:
            if len(group) == 1:
                return 1
            else:
                return 0
        if liste[expected] != "#":
            return solve(liste[expected+1:], group[1:])
        else:
            return 0


def partie1():
    sum = 0
    for line in range(len(data)):
        nums = data[line].split(" ")
        liste = tuple([int(i) for i in nums[1].split(",")])
        ligne = nums[0]
        while ".." in ligne:
            ligne = ligne.replace("..", ".")
        sum += solve(ligne, liste) 
    return sum
def partie2():
    sum = 0
    for line in range(len(data)):
        nums = data[line].split(" ")
        liste = tuple([int(i) for i in nums[1].split(",")]*5)
        ligne = nums[0]+"?"+nums[0]+"?"+nums[0]+"?"+nums[0]+"?"+nums[0]
        while ".." in ligne:
            ligne = ligne.replace("..", ".")
        sum += solve(ligne, liste) 
    return sum

print("Jour 12: \n  Partie 1:", (partie1()), "\n  Partie 2:", (partie2()))
