"""
Advent of Code.

Jour 3 :
Partie 1:
Consigne
diviser par 2 puis trier
"""

file = open("..\\Data\\j3.txt", "r")
lines = [el.strip("\n") for el in file.readlines()]
nline = [[line[:len(line)//2], line[len(line)//2:]] for line in lines]
score = 0
dictio = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}
for ligne in nline:
    for letter in ligne[0]:
        if letter in ligne[1]:
            score += dictio[letter]
            break

print(score)

"""
Partie 2

"""

score = 0
for i in range(len(lines) // 3):

    for letter in lines[i*3]:

        if letter in lines[i*3+1] and letter in lines[i*3+2]:

            score += dictio[letter]
            break

print(score)
