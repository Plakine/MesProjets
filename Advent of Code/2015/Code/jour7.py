data = open("données/jour7.txt").readlines()
for l in range(len(data)):
    data[l] = data[l].strip("\n")
# Partie 1
def read(data):
    instructions = []
    for ligne in range(len(data)):
        if " AND " in data[ligne]:
            instructions.append([1,data[ligne].split(" -> ")[0].split(" AND "), data[ligne].split(" -> ")[1]])
        elif " OR " in data[ligne]:
            instructions.append([2, data[ligne].split(" -> ")[0].split(" OR "), data[ligne].split(" -> ")[1]])
        elif " LSHIFT " in data[ligne]:
            instructions.append([3, data[ligne].split(" -> ")[0].split(" LSHIFT "), data[ligne].split(" -> ")[1]])
        elif " RSHIFT " in data[ligne]:
            instructions.append([4, data[ligne].split(" -> ")[0].split(" RSHIFT "), data[ligne].split(" -> ")[1]])
        elif "NOT " in data[ligne]:
            instructions.append([5, data[ligne].lstrip("NOT ").split(" -> ")[0], data[ligne].lstrip("NOT ").split(" -> ")[1]])
        else:
            instructions.append([6, data[ligne].split(" -> ")[0], data[ligne].split(" -> ")[1]])
    return instructions

def checkneeded(tofind, instructions):
    todo = []
    while len(tofind) > 0:
        for i in range(len(instructions)):
            if instructions[i][2] in tofind:
                if instructions[i] not in todo:
                    todo.append(instructions[i])
                tofind.remove(instructions[i][2])
                if type(instructions[i][1]) is list:
                    for l in range(len(instructions[i][1])):
                        if instructions[i][1][l] not in tofind and instructions[i][1][l].isnumeric() is False:
                            tofind.append(instructions[i][1][l])
                elif instructions[i][1].isnumeric() is False and instructions[i][1] not in tofind:
                    tofind.append(instructions[i][1])
    todo.reverse()
    return todo


def wiring(instructions):
    wires = {}
    while len(instructions) > 0:
        ninstructions = []
        for i in range(len(instructions)):
            if instructions[i][0] == 6:
                try:
                    wires[instructions[i][2]] = int(instructions[i][1])
                except ValueError:
                    try:
                        wires[instructions[i][2]] = wires[instructions[i][1]]
                    except KeyError:
                        ninstructions.append(instructions[i])
            elif instructions[i][0] == 5:
                try:
                    newnum = ""
                    for l in bin(wires[instructions[i][1]]).lstrip("0b"):
                        if l == "0":
                            newnum += "1"
                        else:
                            newnum += "0"
                    while len(newnum) < 16:
                        newnum = "1" + newnum
                    wires[instructions[i][2]] = int(newnum, base=2)
                except KeyError:
                    ninstructions.append(instructions[i])
            elif instructions[i][0] == 4:
                try:
                    wires[instructions[i][2]] = wires[instructions[i][1][0]] >> int(instructions[i][1][1])
                except KeyError:
                    ninstructions.append(instructions[i])
            elif instructions[i][0] == 3:
                try:
                    wires[instructions[i][2]] = wires[instructions[i][1][0]] << int(instructions[i][1][1])
                except KeyError:
                    ninstructions.append(instructions[i])
            elif instructions[i][0] == 2:
                try:
                    wires[instructions[i][2]] = wires[instructions[i][1][0]] | wires[instructions[i][1][1]]
                except KeyError:
                    try:
                        if instructions[i][1][1].isnumeric() and instructions[i][1][0].isnumeric():
                            wires[instructions[i][2]] = int(instructions[i][1][0]) | int(instructions[i][1][1])
                        elif instructions[i][1][1].isnumeric():
                            wires[instructions[i][2]] = wires[instructions[i][1][0]] | int(instructions[i][1][1])
                        elif instructions[i][1][0].isnumeric():
                            wires[instructions[i][2]] = wires[instructions[i][1][1]] | int(instructions[i][1][0])
                        else:
                            ninstructions.append(instructions[i])
                    except KeyError:
                        ninstructions.append(instructions[i])

            elif instructions[i][0] == 1:
                try:
                    wires[instructions[i][2]] = wires[instructions[i][1][0]] & wires[instructions[i][1][1]]
                except KeyError:
                    try:
                        if instructions[i][1][1].isnumeric() and instructions[i][1][0].isnumeric():
                            wires[instructions[i][2]] = int(instructions[i][1][0]) & int(instructions[i][1][1])
                        elif instructions[i][1][1].isnumeric():
                            wires[instructions[i][2]] = wires[instructions[i][1][0]] & int(instructions[i][1][1])
                        elif instructions[i][1][0].isnumeric():
                            wires[instructions[i][2]] = wires[instructions[i][1][1]] & int(instructions[i][1][0])
                        else:
                            ninstructions.append(instructions[i])
                    except KeyError:
                        ninstructions.append(instructions[i])
        instructions = ninstructions
    return wires

def Partie1(tofind, data):
    instructions = read(data)
    instructions = checkneeded(tofind, instructions)
    wires = wiring(instructions)
    return wires["a"]

print(f"Partie 1: {Partie1(['a'], data)}")


def Partie2(tofind, data):
    instructions = read(data)
    instructions = checkneeded(tofind, instructions)
    for i in range(len(instructions)):
        if instructions[i][2] == "b":
            instructions[i][1] = Partie1(["a"], data)
    return wiring(instructions)["a"]

print(f'Partie 2: {Partie2(["a"], data)}')