data = open("data/jour15.txt").read().strip("\n").split(",")

def partie1():
    res = 0
    for i in data:
        current = 0
        for letter in i:
            current = ((current+ord(letter))*17)%256
        res += current
    return res


def partie2():
    res = [[] for i in range(256)]
    res2 = 0
    for i in data:
        current = 0
        if i[-1] == "-":
            tohash = i[:-1]
        else:
            tohash = i[:-2]
        for letter in tohash:
            current = ((current+ord(letter))*17)%256
        if i[-1] != "-":
            f = True
            for j in range(len(res[current])):
                if res[current][j].startswith(i[:-2]):
                    res[current][j] = i.replace("="," ")
                    f = False
            if f:
                res[current].append(i.replace("="," "))
        else:
            for j in range(len(res[current])):
                if res[current][j].startswith(i[:-1]) == True:
                    res[current].pop(j)
                    break
    for i in range(len(res)):
        for j in range(len(res[i])):
            res2 += (i+1)*(j+1)*int(res[i][j][-1])
    return res2


print("Jour 15: \n  Partie 1:", (partie1()), "\n  Partie 2:", (partie2()))
