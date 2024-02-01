data = open("data/jour21.txt").read().splitlines()


def find_S(grille):
    for line in range(len(grille)):
        for colonne in range(len(grille[line])):
            if grille[line][colonne] == "S":
                return (line, colonne)
    raise ValueError("Couldn't find S")


def partie1(grille, walk_value):
    values = [find_S(grille)]
    even = [values[0]]
    odd = []
    for _ in range(walk_value):
        nv = []
        if (_+1)%2==0:
            for value in values:
                y = value[0]
                x = value[1]
                if x > 0 and grille[y][x-1] in ".S" and (y, x-1) not in even:
                    nv.append((y, x-1))
                    even.append(nv[-1])
                if x < len(grille[y])-1 and grille[y][x+1] in ".S" and (y, x+1) not in even:
                    nv.append((y, x+1))
                    even.append(nv[-1])
                if y > 0 and grille[y-1][x] in ".S" and (y-1, x) not in even:
                    nv.append((y-1, x))
                    even.append(nv[-1])
                if y < len(grille)-1 and grille[y+1][x] in ".S" and (y+1, x) not in even:
                    nv.append((y+1, x))
                    even.append(nv[-1])

        elif (_+1)%2==1:
            for value in values:
                y = value[0]
                x = value[1]
                if x > 0 and grille[y][x-1] in ".S" and (y, x-1) not in odd:
                    nv.append((y, x-1))
                    odd.append(nv[-1])
                if x < len(grille[y])-1 and grille[y][x+1] in ".S" and (y, x+1) not in odd:
                    nv.append((y, x+1))
                    odd.append(nv[-1])
                if y > 0 and grille[y-1][x] in ".S" and (y-1, x) not in odd:
                    nv.append((y-1, x))
                    odd.append(nv[-1])
                if y < len(grille)-1 and grille[y+1][x] in ".S" and (y+1, x) not in odd:
                    nv.append((y+1, x))
                    odd.append(nv[-1])
        values = nv
    if walk_value % 2 == 0:
        return len(even)
    else:
        return len(odd)



def partie2(data):
    fullsize_even = partie1(data, 132)
    fullsize_odd = partie1(data, 133)
    corners_even = fullsize_even-partie1(data, 64)
    corners_odd = fullsize_odd-partie1(data, 65)
    n = 202300
    return ((n+1)**2)*fullsize_odd + (n**2)*fullsize_even - (n+1)*corners_odd+n*corners_even

print(partie1(data, 64))
print(partie2(data))


