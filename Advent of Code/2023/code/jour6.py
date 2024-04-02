from math import sqrt, ceil
data = open("data/jour6.txt").read().splitlines()


def partie1():
    psum = 1
    num1 = data[0].strip("Time:        ").split("     ")
    num2 = data[1].lstrip("Distance:   ").split("   ")
    for i in range(len(num1)):
        a = -1
        b = int(num1[i])
        c = -int(num2[i])
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = int(((-b+sqrt(delta))/(2*a))+1)
            x2 = ceil(((-b-sqrt(delta))/(2*a))-1)
            psum *= x2-x1+1
    return psum


def partie2():
    psum = 1
    num1 = data[0].strip("Time:        ")
    num1 = int(num1.replace(" ", ""))
    num2 = data[1].lstrip("Distance:   ")
    num2 = int(num2.replace(" ", ""))
    a = -1
    b = num1
    c = -num2
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = int(((-b+sqrt(delta))/(2*a))+1)
        x2 = ceil(((-b-sqrt(delta))/(2*a))-1)
        psum *= x2-x1+1
    return psum


print("Jour 6: \n  Partie 1:", (partie1()), "\n  Partie 2:", (partie2()))
