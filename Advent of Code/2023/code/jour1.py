
data = open("data\\jour1.txt")
data = data.readlines()
for i in range(len(data)):
    data[i] = data[i].strip("\n")

# Partie 1
res = 0
for ligne in range(len(data)):
    res1 = ''
    i = 0
    while i < len(data[ligne]):
        if data[ligne][i] in "123456789":
            res1 += data[ligne][i]
        i += 1
    res += (int(res1[0] + res1[-1]))


# Partie 2
res1 = 0
d1 = {"one": "1", "two": "2", "six": "6"}
d2 = {"four": "4", "five": "5", "nine": "9"}
d3 = {"three": "3", "seven": "7", "eight": "8"}
for ligne in range(len(data)):
    res = ""
    for i in range(len(data[ligne])):
        if i < len(data[ligne])-2:
            if data[ligne][i:i+3] in d1.keys():
                res += d1[data[ligne][i:i+3]]
        if i < len(data[ligne])-3:
            if data[ligne][i:i+4] in d2.keys():
                res += d2[data[ligne][i:i+4]]
        if i < len(data[ligne])-4:
            if data[ligne][i:i+5] in d3.keys():
                res += d3[data[ligne][i:i+5]]
        if data[ligne][i] in "123456789":
            res += data[ligne][i]
    res1 += (int(res[0]+res[-1]))

print("Jour 1: \n  Partie 1:", (res), "\n  Partie 2:", (res1))
