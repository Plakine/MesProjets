from random import randint

def v1(input):
    sentence = str(input).split(" ")
    for mot in sentence:
        mot = "".join(["*" if lettre in mot[1:-1] else lettre for lettre in mot])
        print(mot)


def v2():
    str = "La roue de la fortune".split(" ")
    for f in str:
        f = "".join(["*" if randint(0,100) in range(50) else e for e in f])
        print(f)

