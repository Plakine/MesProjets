"""
Jour 5
"""

data = open("data/jour5.txt").read()
data = data.splitlines()


def partie1():
    data.append("")
    graines = data[0].lstrip("seeds: ").split(" ")
    for i in range(len(graines)):
        graines[i] = int(graines[i])
    ngraines = []
    for line in data[2:]:
        if line == "":
            for graine in ngraines:
                graines.append(int(graine))
            ngraines = []
        elif line[-1] != ":":
            ranges = line.split(" ")
            for i in range(len(graines)):
                if int(graines[i]) >= int(ranges[1]) and\
                      int(graines[i]) <= int(ranges[1]) + int(ranges[2]):
                    ngraines.append(int(ranges[0]) + (int(graines[i])
                                                      - int(ranges[1])))
                    graines[i] = ""
        for i in range(len(graines)-1, -1, -1):
            if graines[i] == "":
                graines.pop(i)
    return min(graines)


def partie2():
    data.append("")
    g = data[0].lstrip("seeds : ").split(" ")
    seeds = []
    for i in range(len(g)//2):
        # [a, b[
        seeds.append((int(g[i*2]), int(g[i*2])+int(g[i*2+1])))
    del g
    nseeds = []
    for line in data[2:]:
        if line == "":
            for graine in nseeds:
                seeds.append(graine)
            nseeds = []
        elif line[-1] != ":":
            ranges = line.split(" ")
            a = int(ranges[0])
            b = int(ranges[1])
            c = int(ranges[2])
            for i in range(len(seeds)):
                d = seeds[i][0]
                e = seeds[i][1]
                if d >= e:
                    seeds[i] = ""
                if b <= d and b+c >= e and d < e:
                    # Cas [d,e[ C [b, b+c[
                    nseeds.append((a+(d-b), a+e-b))
                    seeds[i] = ""
                elif b >= d and b+c <= e and d < e:
                    nseeds.append((a, a+c))
                    seeds.append((d, b))
                    seeds.append((b+c, e))
                    seeds[i] = ""
                elif b <= d and b+c <= e and b+c > d and d <= b+c and d < e:
                    nseeds.append((a+d-b, a+c))
                    seeds.append((b+c, e))
                    seeds[i] = ""
                elif b >= d and b+c >= e and b < e and d < e:
                    nseeds.append((a, a+(e-b)))
                    seeds.append((d, b))
                    seeds[i] = ""
            for j in range(len(seeds)-1, -1, -1):
                if seeds[j] == "":
                    seeds.pop(j)
    min = seeds[0][0]
    for i in range(len(seeds)):
        if seeds[i][0] < min:
            min = seeds[i][0]
    return min


print("Jour 5: \n  Partie 1:", (partie1()), "\n  Partie 2:", (partie2()))
