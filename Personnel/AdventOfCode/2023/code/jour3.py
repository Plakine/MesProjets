"""
jour 3
"""
data = open("data\\jour3.txt")
data = data.readlines()
for i in range(len(data)):
    data[i] = data[i].strip('\n')


def part1():
    res = 0
    for line in range(len(data)):
        nums = []
        cnum = ""
        pos = []
        for j in range(len(data[line])):
            if data[line][j] in "0123456789":
                cnum += data[line][j]
                pos.append(j)
            else:
                if cnum != "":
                    nums.append((cnum, pos))
                    cnum = ""
                    pos = []
        if cnum != "":
            nums.append((cnum, pos))
            cnum = ""
            pos = []
        for num in nums:
            f = False
            if line > 0:
                if num[1][0] > 0:
                    if data[line-1][num[1][0]-1] != ".":
                        f = True
                if num[1][-1] < len(data[line])-1:
                    if data[line-1][num[1][-1]+1] != ".":
                        f = True
                for pos in num[1]:
                    if data[line-1][pos] != ".":
                        f = True
            if line < len(data)-1:
                if num[1][0] > 0:
                    if data[line+1][num[1][0]-1] != ".":
                        f = True
                if num[1][-1] < len(data[line])-1:
                    if data[line+1][num[1][-1]+1] != ".":
                        f = True
                for pos in num[1]:
                    if data[line+1][pos] != ".":
                        f = True
            if num[1][0] > 0:
                if data[line][num[1][0]-1] != ".":
                    f = True
            if num[1][-1] < len(data[line])-1:
                if data[line][num[1][-1]+1] != ".":
                    f = True
            if f:
                res += int(num[0])
    return (res)


def partie2():
    res = 0
    pos = []
    numerals = []
    for line in range(len(data)):
        nums = []
        cnum = ""
        pos2 = []
        for j in range(len(data[line])):
            if data[line][j] in "0123456789":
                cnum += data[line][j]
                pos2.append(j)
            else:
                if cnum != "":
                    nums.append((cnum, pos2))
                    cnum = ""
                    pos2 = []
        if cnum != "":
            nums.append((cnum, pos2))
            cnum = ""
            pos2 = []
        numerals.append(nums)
        for j in range(len(data[line])):
            if data[line][j] == "*":
                pos.append((line, j))
    for ligne, col in pos:
        sets = []
        if ligne > 0:
            for num in numerals[ligne-1]:
                for pos1 in num[1]:
                    if pos1 in [col-1, col+1, col]:
                        sets.append(num)
                        break
        if ligne < len(data)-1:
            for num in numerals[ligne+1]:
                for pos1 in num[1]:
                    if pos1 in [col-1, col+1, col]:
                        sets.append(num)
                        break
        for num in numerals[ligne]:
            for pos1 in num[1]:
                if pos1 in [col-1, col+1]:
                    sets.append(num)
                    break
        if len(sets) == 2:
            res += int(sets[0][0]) * int(sets[1][0])
    return res


print("Jour 3: \n  Partie 1:", (part1()), "\n  Partie 2:", (partie2()))
