from math import lcm

data = open("data/jour8.txt").read().splitlines()


def partie1(start='AAA', end="ZZZ"):
    instructions = data[0].replace("L", '0').replace("R", "1")
    dic = {}
    for line in data[2:]:
        ins = line.split(" = ")
        ins[1] = ins[1].strip("()")
        ins[1] = ins[1].split(", ")
        dic[ins[0]] = (ins[1][0], ins[1][1])
    current = start
    i = 0
    condition_matched = False
    while not condition_matched:
        current = dic[current][int(instructions[i % len(instructions)])]
        i = (i+1)
        if (end == "ZZZ" and current == end) or\
                (end != "ZZZ" and current[-1] == "Z"):
            condition_matched = True
    return i


def partie2():
    numbers = []
    for line in data[2:]:
        if line[2] == "A":
            numbers.append(partie1(line[:3], "Z"))
    return lcm(*numbers)


print("Jour 8: \n  Partie 1:", (partie1()), "\n  Partie 2:", (partie2()))
