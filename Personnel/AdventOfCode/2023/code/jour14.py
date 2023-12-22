data = open("data/jour14.txt").read().splitlines()
def partie1():
    Roches = []
    res = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "O":
                for i_2 in range(i-1, -15, -1):
                    if data[i_2][j] != "." or i_2 == -1:
                        Roches.append((i_2+1, j))
                        data[i] = data[i][:j] + "." + data[i][j+1:]
                        data[i_2+1] = data[i_2+1][:j] + "O" + data[i_2+1][j+1:]
                        break
    for caillou in Roches:
        res += len(data)-caillou[0]
    return res
def partie2():
    res = 0
    count = 0
    previous_cycles = [[data[i] for i in range(len(data))]]
    while count < 1000:
        count += 1
        # North
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == "O":
                    for i_2 in range(i-1, -15, -1):
                        if data[i_2][j] != "." or i_2 == -1:
                            data[i] = data[i][:j] + "." + data[i][j+1:]
                            data[i_2+1] = data[i_2+1][:j] + "O" + data[i_2+1][j+1:]
                            break
        #OUEST
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i] = data[i].replace(".O", "O.")
        # Sud
        for i in range(len(data)-1, -1, -1):
            for j in range(len(data[i])):
                if data[i][j] == "O":
                    for i_2 in range(i+1, len(data)+1):
                        if i_2 == len(data) or data[i_2][j] != ".":
                            data[i] = data[i][:j] + "." + data[i][j+1:]
                            data[i_2-1] = data[i_2-1][:j] + "O" + data[i_2-1][j+1:]
                            break
        for i in range(len(data)):
            for j in range(len(data[i])):
                data[i] = data[i].replace("O.", ".O")
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "O":
                res += len(data)-i
    return res

e = partie1()
data = open("data/jour14.txt").read().splitlines()
print("Jour 14: \n  Partie 1:", (e), "\n  Partie 2:", (partie2()))
