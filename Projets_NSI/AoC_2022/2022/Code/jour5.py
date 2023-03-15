"""
Advent of code.

jour 5
"""

files = open("..\Data\j5.txt")
lines = [el.strip('\n') for el in files.readlines()]
caisses = lines[:lines.index("")-1]
caisse = [[caisses[i][1+4*k] for i in range(len(caisses)-1,-1,-1)] for k in range(9)]
for i in range(len(caisse)):
    while caisse[i][-1] == " ":
        caisse[i].pop()
directions = lines[lines.index("")+1:]
quantity =[]
source = []
destination = []
for i in directions:
    if len(i) == 18:
        quantity.append(int(i[5]))
        source.append(int(i[12]))
    else:
        quantity.append(int(i[5:7]))
        source.append(int(i[13]))
        
    destination.append(int(i[-1]))
for i in range(len(quantity)):
    crane = []
    print(caisse[source[i]],quantity[i])
    crane.append(caisse[source[i]][-quantity[i]:])
    while len(crane) <0:
        caisse[destination[i-1]].append(crane[0][-1])
        crane[0].pop()