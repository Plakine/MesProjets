"""
Julien Antognelli
Advent of Code
jour 3
"""

# On lit les données
data = open("données/jour3.txt").readline()
# Partie 1
def part1(data):
    visited_house = [[0,0]]
    coordinates = [0, 0] # ([hautbas, droitegauche])
    for i in data:
        if i == ">":
            coordinates[1] += 1
        elif i == "<":
            coordinates[1] -= 1
        elif i == "^":
            coordinates[0] -= 1
        else:
            coordinates[0] += 1
        if coordinates not in visited_house:
            visited_house.append([coordinates[0], coordinates[1]])
    return len(visited_house)

print(f"Partie 1 : {part1(data)}")


# Partie 2
def partie2(data):
    visited_house = [[0,0]]
    coordinates1 = [0, 0] # ([hautbas, droitegauche])
    coordinates2 = [0, 0]
    for i in range(len(data)):
        if i%2 == 0:
            if data[i] == ">":
                coordinates1[1] += 1
            elif data[i] == "<":
                coordinates1[1] -= 1
            elif data[i] == "^":
                coordinates1[0] -= 1
            else:
                coordinates1[0] += 1
            if coordinates1 not in visited_house:
                visited_house.append([coordinates1[0], coordinates1[1]])
        else:
            if data[i] == ">":
                coordinates2[1] += 1
            elif data[i] == "<":
                coordinates2[1] -= 1
            elif data[i] == "^":
                coordinates2[0] -= 1
            else:
                coordinates2[0] += 1
            if coordinates2 not in visited_house:
                visited_house.append([coordinates2[0], coordinates2[1]])
    return len(visited_house)

print(f"Partie 2: {partie2(data)}")