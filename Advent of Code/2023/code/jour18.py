data = open("data/jour18.txt").read().splitlines()

def partie2():
    x = 0
    y = 0
    points = [(0,0)]
    for line in data:
        text = line.split(" ")[2].strip("()")
        if text[-1] == "0":
            direction = "R"
        elif text[-1] == "1":
            direction = "D"
        elif text[-1] == "2":
            direction = "L"
        elif text[-1] == "3":
            direction = "U"
        repetitions = int(text[1:-1], 16)
        directions = {
            "U": (0, 1),
            "D": (0, -1),
            "L": (-1, 0),
            "R": (1, 0),
        }
        x = x + directions[direction][0]*repetitions
        y = y + directions[direction][1]*repetitions
        points.append((x, y))
    co1, co2 = 0,0
    c2 = 0
    for i in range(len(points)-1):
        co1 += points[i][0]*points[i+1][1]
        co2 += points[i+1][0]*points[i][1]
        c2 += abs(points[i][0]-points[i+1][0])+abs(points[i][1]-points[i+1][1])
    count = 0.5*abs(co1-co2)
    return int(count+0.5*c2+1)

def partie1():
    x = 0
    y = 0
    points = [(0,0)]
    for line in data:
        direction, repetitions = line.split(" ")[:2]
        repetitions = int(repetitions)
        directions = {
            "U": (0, 1),
            "D": (0, -1),
            "L": (-1, 0),
            "R": (1, 0),
        }
        x = x + directions[direction][0]*repetitions
        y = y + directions[direction][1]*repetitions
        points.append((x, y))
    co1, co2 = 0,0
    c2 = 0
    for i in range(len(points)-1):
        co1 += points[i][0]*points[i+1][1]
        co2 += points[i+1][0]*points[i][1]
        c2 += abs(points[i][0]-points[i+1][0])+abs(points[i][1]-points[i+1][1])
    count = 0.5*abs(co1-co2)
    return int(count+0.5*c2+1)


print("Jour 18: \n  Partie 1:", (partie1()), "\n  Partie 2:", (partie2()))
