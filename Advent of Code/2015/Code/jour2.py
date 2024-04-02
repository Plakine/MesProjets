"""
Julien Antognelli
Advent of Code
jour 2
"""
# On lit les données
data = open("données/jour2.txt")
data = data.readlines()
for line in range(len(data)):
    data[line] = data[line].strip("\n").split("x")
    for num in range(len(data[line])):
        data[line][num] = int(data[line][num])
    # On mets les donneés sous forme [l,w,h]


# Partie 1
def Part1(data):
    res = 0
    for l in data:
        cote1 = l[0]*l[1]
        cote2 = l[1]*l[2]
        cote3 = l[2]*l[0]
        res += 2*(cote1+cote2+cote3)  # 2*l*w + 2*w*h + 2*h*l
        if cote1 <= cote2 and cote1 <= cote3:
            res += cote1
        elif cote2 <= cote1 and cote2 <= cote3:
            res += cote2
        else:
            res += cote3
    return res
        

print(f"Partie 1 : {Part1(data)}")


# Partie 2
def partie2(data):
    res = 0
    for l in data:
        res += l[0]*l[1]*l[2]
        if l[0]*l[1] <= l[1]*l[2] and l[0]*l[1]<= l[2]*l[0]:
            res += 2*(l[0]+l[1])
        elif l[1]*l[2] <= l[0]*l[1] and l[1]*l[2] <= l[2]*l[0]:
            res += 2*(l[1]+l[2])
        else:
            res += 2*(l[2]+l[0])
    return res

print(f"Partie 2 : {partie2(data)}")