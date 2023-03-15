"""
Advent of code.

jour 4
partie 1
"""
file = open("..\\Data\\j4.txt", "r")
lines = [line.strip("\n") for line in file.readlines()]
values = [elem.split(",") for elem in lines]
values = [[j[0].split("-"), j[1].split("-")] for j in values]
dwarf1 = [el[0] for el in values]
dwarf2 = [el[1] for el in values]
score = 0
for i in range(len(dwarf1)):
    if (int(dwarf1[i][0]) <= int(dwarf2[i][0])
            and int(dwarf2[i][1]) <= int(dwarf1[i][1])):
        score += 1
    elif (int(dwarf2[i][0]) <= int(dwarf1[i][0])
          and int(dwarf1[i][1]) <= int(dwarf2[i][1])):
        score += 1
    else:
        print(dwarf1[i], dwarf2[i])
print(score)

"""
partie 2
"""


score = 0
for i in range(len(dwarf1)):
    if (int(dwarf1[i][0]) <= int(dwarf2[i][0])
            and int(dwarf2[i][0]) <= int(dwarf1[i][1])):
        score += 1
    elif (int(dwarf1[i][0]) <= int(dwarf2[i][1])
            and int(dwarf2[i][1]) <= int(dwarf1[i][1])):
        score += 1
    elif (int(dwarf2[i][0]) <= int(dwarf1[i][1])
          and int(dwarf1[i][1]) <= int(dwarf2[i][1])):
        score += 1
    elif (int(dwarf2[i][0]) <= int(dwarf1[i][0])
          and int(dwarf1[i][0]) <= int(dwarf2[i][1])):
        score += 1
print(score)
