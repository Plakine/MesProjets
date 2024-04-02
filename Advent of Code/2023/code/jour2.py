"""
jour 2
"""
data = open("data\\jour2.txt")
data = data.readlines()
for i in range(len(data)):
    data[i] = data[i].strip('\n')


def part1():
    res = 0
    for line in data:
        val = line.split(":")
        val[0] = val[0].lstrip("Game ")
        res += int(val[0])
        sets = val[1].split(";")
        for j in range(len(sets)):
            dic = {"red": 0, "green": 0, "blue": 0}
            colors = sets[j].split(",")
            for f in range(len(colors)):
                colors[f] = colors[f].lstrip(" ").split(" ")
                colors[f][1] = colors[f][1]
                dic[colors[f][1]] += int(colors[f][0])
            if dic["red"] >= 13 or dic["green"] >= 14 or dic["blue"] >= 15:
                res -= int(val[0])
                break
    return res


def part2():
    pres = 0
    for line in data:
        val = line.split(":")
        val[0] = val[0].lstrip("Game ")
        sets = val[1].split(";")
        ming = 0
        minr = 0
        minb = 0
        for j in range(len(sets)):
            dic = {"red": 0, "green": 0, "blue": 0}
            colors = sets[j].split(",")
            for f in range(len(colors)):
                colors[f] = colors[f].lstrip(" ").split(" ")
                colors[f][1] = colors[f][1]
                dic[colors[f][1]] += int(colors[f][0])
                if ming < dic["green"]:
                    ming = dic["green"]
                if minr < dic["red"]:
                    minr = dic["red"]
                if minb < dic["blue"]:
                    minb = dic["blue"]
        pres += minr*minb*ming
    return pres


print("Jour 2: \n  Partie 1:", (part1()), "\n  Partie 2:", (part2()))
