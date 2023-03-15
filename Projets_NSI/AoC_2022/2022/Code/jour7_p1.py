"""
AOC jour 7.

partie 1
"""
data = [el.strip("\n") for el in open("...\\Data\\j7.txt", "r").readlines()]
dirname = "./"
dirsize = 0
sizes = {}
directoriesinside = {}
fulldirectory = []
for i in data:
    if i[0] == "$":
        if (i[2:4] == "cd"):
            if i[5:] != "..":
                f = i[5:]
                while f in directoriesinside:
                    f += "_1"
                fulldirectory.append(f)
                sizes[dirname] = dirsize
                dirsize = 0
                dirname = f
                directoriesinside[f] = []
            else:
                sizes[dirname] = dirsize
                fulldirectory.pop()
                dirname = fulldirectory[-1]
                dirsize = sizes[dirname]
    else:
        if i[0:3] == "dir":
            f = i[4:]
            while f in directoriesinside:
                f += "_1"
            directoriesinside[dirname].append(f)
        else:
            space = i.index(" ")
            dirsize += int(i[:space])
sizes[dirname] = dirsize
size = 0


for i in range(len(directoriesinside)):
    if list(directoriesinside.items())[-i-1][1] != []:
        if len(list(directoriesinside.items())[-i-1][1]) ==1:
            sizes[list(directoriesinside.items())[-i-1][0]] += sizes[list(directoriesinside.items())[-i-1][1][0]]
        else:
            for l in range(len(list(directoriesinside.items())[-i-1][1])):
                sizes[list(directoriesinside.items())[-i-1][0]] += sizes[list(directoriesinside.items())[-i-1][1][l]]
for i in sizes:
    if sizes[i] <= 100000:
        size += sizes[i]
print(size)