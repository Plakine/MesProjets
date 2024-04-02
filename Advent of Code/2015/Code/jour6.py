"""
Julien Antognelli
Advent of code
jour 6
"""

data = open("données/jour6.txt").readlines()
for l in range(len(data)):
    data[l] = data[l].strip("\n")

databis = open("données/jour6.txt").readlines()
for l in range(len(databis)):
    databis[l] = databis[l].strip("\n")


def Partie1(data):
    grid = [[0 for i in range(1000)] for l in range(1000)]
    for line in range(len(data)):
        if "turn on" in data[line]:
            data[line] = data[line][8:]
            instruction = data[line].split(" through ")
            for i in range(len(instruction)):
                instruction[i] = instruction[i].split(",")
                for l in range(len(instruction[i])):
                    instruction[i][l] = int(instruction[i][l])
            for l in range(instruction[0][0], instruction[1][0]+1):
                for c in range(instruction[0][1],instruction[1][1]+1):
                    grid[l][c] = 1
        if "turn off" in data[line]:
            data[line] = data[line][9:]
            instruction = data[line].split(" through ")
            for i in range(len(instruction)):
                instruction[i] = instruction[i].split(",")
                for l in range(len(instruction[i])):
                    instruction[i][l] = int(instruction[i][l])
            for l in range(instruction[0][0], instruction[1][0]+1):
                for c in range(instruction[0][1],instruction[1][1]+1):
                    grid[l][c] = 0
        if "toggle" in data[line]:
            data[line] = data[line][7:]
            instruction = data[line].split(" through ")
            for i in range(len(instruction)):
                instruction[i] = instruction[i].split(",")
                for l in range(len(instruction[i])):
                    instruction[i][l] = int(instruction[i][l])
            for l in range(instruction[0][0], instruction[1][0]+1):
                for c in range(instruction[0][1],instruction[1][1]+1):
                    grid[l][c] = (grid[l][c]+1)%2
    res = 0
    for l in range(len(grid)):
        for c in range(len(grid[l])):
            if grid[l][c] == 1:
                res += 1
    return res

print(f"partie 1: {Partie1(data)}")


def partie2(data):
    grid = [[0 for i in range(1000)] for l in range(1000)]
    for line in range(len(data)):
        if "turn on" in data[line]:
            data[line] = data[line][8:]
            instruction = data[line].split(" through ")
            for i in range(len(instruction)):
                instruction[i] = instruction[i].split(",")
                for l in range(len(instruction[i])):
                    instruction[i][l] = int(instruction[i][l])
            for l in range(instruction[0][0], instruction[1][0]+1):
                for c in range(instruction[0][1],instruction[1][1]+1):
                    grid[l][c] = grid[l][c] + 1
        if "turn off" in data[line]:
            data[line] = data[line][9:]
            instruction = data[line].split(" through ")
            for i in range(len(instruction)):
                instruction[i] = instruction[i].split(",")
                for l in range(len(instruction[i])):
                    instruction[i][l] = int(instruction[i][l])
            for l in range(instruction[0][0], instruction[1][0]+1):
                for c in range(instruction[0][1],instruction[1][1]+1):
                    if grid[l][c] != 0:
                        grid[l][c] = grid[l][c] - 1
        if "toggle" in data[line]:
            data[line] = data[line][7:]
            instruction = data[line].split(" through ")
            for i in range(len(instruction)):
                instruction[i] = instruction[i].split(",")
                for l in range(len(instruction[i])):
                    instruction[i][l] = int(instruction[i][l])
            for l in range(instruction[0][0], instruction[1][0]+1):
                for c in range(instruction[0][1],instruction[1][1]+1):
                    grid[l][c] = grid[l][c]+2
    res = 0
    for l in range(len(grid)):
        for c in range(len(grid[l])):
            res += grid[l][c]
    return res

print(f"Partie 2: {partie2(databis)}")