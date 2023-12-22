data = open("data/jour9.txt").read().splitlines()


def jour9():
    sum = 0
    sum2 = 0
    for line in data:
        line_data = line.split(" ")
        sublines = [line_data]
        flag = True
        while flag:
            csub = []
            continu = False
            for i in range(len(sublines[-1])-1):
                csub.append(int(sublines[-1][i+1])-int(sublines[-1][i]))
                if int(sublines[-1][i+1])-int(sublines[-1][i]) != 0:
                    continu = True
            flag = continu
            sublines.append(csub)
        add2 = 0
        for line in range(len(sublines)-1, -1, -1):
            sum += int(sublines[line][-1])
            add2 = int(sublines[line][0]) - add2
        sum2 += add2
    return sum, sum2


a, b = jour9()
print("Jour 9: \n  Partie 1:", a, "\n  Partie 2:", b)
