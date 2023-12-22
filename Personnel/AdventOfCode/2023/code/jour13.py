import numpy as np
data = open("data/jour13.txt").readlines()
patterns = []
temp = []
for i in range(len(data)):
    if data[i] == "\n":
        patterns.append(temp)
        temp = []
    else:
        num = []
        for char in data[i].strip("\n"):
            if char == ".":
                num.append(0)
            else:
                num.append(1)
        temp.append(num)
if temp != []:
    patterns.append(temp)
    temp = []

for i in range(len(patterns)):
    patterns[i] = np.array(patterns[i])


def searchpatter(pattern):
    res = []
    nextline = 0
    while 1:
        line = None
        for i in range(nextline, len(pattern)):
            if i > 0 and (pattern[i] == pattern[i-1]).all():
                line = i
                break
        if line is None:
            return res
        else:
            nextline = line+1
        flag = True
        for i in range(line, len(pattern)):
            if 2*line-i-1 >= 0 and not (pattern[i] == pattern[2*line-i-1]).all():
                flag = False
        if flag:
            res.append(line)
def differences(p1, p2):
    res = 0
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            res += 1
    return res
def searchpatter_2(pattern):
    res = []
    nextline = 0
    while nextline < len(pattern):
        maxdiff = 1
        line = None
        for i in range(nextline, len(pattern)):
            if i > 0 and differences(pattern[i], pattern[i-1]) <= maxdiff and i not in searchpatter(pattern):
                line = i
                maxdiff -= differences(pattern[i], pattern[i-1])
                break
        if maxdiff == 0:
            maxdiff += 1
        if line == None:
            res.append(False)
            line = len(pattern)
        for i in range(line, len(pattern)):
            if 2*line-i-1 >= 0 and not differences(pattern[i],pattern[2*line-i-1]) <= maxdiff:
                res.append(False)
                maxdiff = 5
                break
            if differences(pattern[i],pattern[2*line-i-1]) <= maxdiff:
                maxdiff -= differences(pattern[i],pattern[2*line-i-1])
        if maxdiff == 0:
            return line
        else:
            nextline = line+1
            res.append(False)
    return res

def partie1():
    res = 0
    for pattern in patterns:
        reverse_p = np.transpose(pattern)
        sum1 = searchpatter(pattern)
        sum2 = searchpatter(reverse_p)
        for sum in sum1:
            res += sum*100
        for sum in sum2:
            res += sum
    return res

def partie2():
    res = 0
    for pattern in patterns:
        reverse_p = np.transpose(pattern)
        sum1 = searchpatter_2(pattern)
        sum2 = searchpatter_2(reverse_p)
        if sum1 is list and sum2 is list:
            raise ValueError(pattern)
        if type(sum1) is not list:
            res += sum1*100
        if type(sum2) is not list:
            res += sum2
    return res

print("Jour 13: \n  Partie 1:", (partie1()), "\n  Partie 2:", (partie2()))
