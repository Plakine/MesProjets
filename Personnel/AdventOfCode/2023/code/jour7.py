"""
AOC jour 7
"""

data = open("data/jour7.txt").read().splitlines()


def partie1():
    somme = 0
    five = []
    four = []
    full = []
    three = []
    dual_pair = []
    pair = []
    high = []
    for line in data:
        line = line.replace("A", "e")
        line = line.replace("K", "d")
        line = line.replace("Q", "c")
        line = line.replace("J", "b")
        line = line.replace("T", "a")
        nums = line.split(" ")
        dic = {}
        score = int(nums[0], 16)
        for j in nums[0]:
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
        vals = list(dic.values())
        vals.sort()
        if vals == [5]:
            five.append((score, int(nums[1])))
        elif vals == [1, 4]:
            four.append((score, int(nums[1])))
        elif vals == [2, 3]:
            full.append((score, int(nums[1])))
        elif vals == [1, 1, 3]:
            three.append((score, int(nums[1])))
        elif vals == [1, 2, 2]:
            dual_pair.append((score, int(nums[1])))
        elif vals == [1, 1, 1, 2]:
            pair.append((score, int(nums[1])))
        else:
            high.append((score, int(nums[1])))
    for liste in [five, four, full, three, dual_pair, pair, high]:
        liste.sort(key=lambda a: a[0])
    compteur = 1
    cards = high + pair + dual_pair + three + full + four + five
    for i in cards:
        somme += i[1]*compteur
        compteur += 1
    return somme


def partie2():
    somme = 0
    five = []
    four = []
    full = []
    three = []
    dual_pair = []
    pair = []
    high = []
    for line in data:
        line = line.replace("A", "e")
        line = line.replace("K", "d")
        line = line.replace("Q", "c")
        line = line.replace("J", "0")
        line = line.replace("T", "a")
        nums = line.split(" ")
        dic = {}
        score = int(nums[0], 16)
        joker = 0
        for j in nums[0]:
            if j == "0":
                joker += 1
            elif j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
        vals = list(dic.values())
        vals.sort()
        if joker < 5:
            vals[-1] += joker
        else:
            vals = [5]
        if vals == [5]:
            five.append((score, int(nums[1])))
        elif vals == [1, 4]:
            four.append((score, int(nums[1])))
        elif vals == [2, 3]:
            full.append((score, int(nums[1])))
        elif vals == [1, 1, 3]:
            three.append((score, int(nums[1])))
        elif vals == [1, 2, 2]:
            dual_pair.append((score, int(nums[1])))
        elif vals == [1, 1, 1, 2]:
            pair.append((score, int(nums[1])))
        else:
            high.append((score, int(nums[1])))
    for liste in [five, four, full, three, dual_pair, pair, high]:
        liste.sort(key=lambda a: a[0])
    compteur = 1
    cards = high + pair + dual_pair + three + full + four + five
    for i in cards:
        somme += i[1]*compteur
        compteur += 1
    return somme


print("Jour 7: \n  Partie 1:", (partie1()), "\n  Partie 2:", (partie2()))
