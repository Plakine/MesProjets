data = open("data/jour11.txt").read().splitlines()

def partie1():
    galaxies = []
    lines = [0]
    columns = []
    for line in range(len(data)):
        for char in range(len(data[line])):
            if data[line][char] == "#":
                galaxies.append((line, char))
                if lines[-1] != line:
                    lines.append(line)
                if char not in columns:
                    columns.append(char)
    lignebarre = [i for i in range(len(data)) if i not in lines]
    columnsbar = [i for i in range(len(data[0])) if i not in columns]
    i = 0
    sum = 0
    for j in range(len(galaxies)):
        while i < len(lignebarre) and galaxies[j][0] > lignebarre[i]:
            i += 1
        newgalaxy = galaxies[j][0] + i
        v = 0
        while v < len(columnsbar) and galaxies[j][1] > columnsbar[v]:
            v += 1
        newgalaxx = galaxies[j][1] + v
        galaxies[j] = (newgalaxy, newgalaxx)
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            sum += abs(galaxies[i][1]-galaxies[j][1]) + abs(galaxies[i][0] - galaxies[j][0])
    return sum      


def partie2():
    galaxies = []
    lines = [0]
    columns = []
    for line in range(len(data)):
        for char in range(len(data[line])):
            if data[line][char] == "#":
                galaxies.append((line, char))
                if lines[-1] != line:
                    lines.append(line)
                if char not in columns:
                    columns.append(char)
    lignebarre = [i for i in range(len(data)) if i not in lines]
    columnsbar = [i for i in range(len(data[0])) if i not in columns]
    i = 0
    sum = 0
    for j in range(len(galaxies)):
        while i < len(lignebarre) and galaxies[j][0] > lignebarre[i]:
            i += 1
        newgalaxy = galaxies[j][0] + i*(1000000-1)
        v = 0
        while v < len(columnsbar) and galaxies[j][1] > columnsbar[v]:
            v += 1
        newgalaxx = galaxies[j][1] + v*(1000000-1)
        galaxies[j] = (newgalaxy, newgalaxx)
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            sum += abs(galaxies[i][1]-galaxies[j][1]) + abs(galaxies[i][0] - galaxies[j][0])
    return sum      


print("Jour 11: \n  Partie 1:", (partie1()), "\n  Partie 2:", (partie2()))
