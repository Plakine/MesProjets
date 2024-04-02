"""
Projet calculateur
Julien Antognelli
"""
from math import cos, sin, tan, acos, asin, atan, sinh, cosh, tanh, log, log10, sqrt, e, pi, atan2


class Complexes:
    def __init__(self, re, im) -> None:
        self.reel = re
        self.imaginaire = im
        self.module = sqrt(self.reel**2 + self.imaginaire**2)
        self.argument = atan2(self.reel, self.imaginaire)

    def __repr__(self) -> str:
        if self.reel != 0:
            if self.imaginaire > 0:
                return f"{self.reel}+{self.imaginaire}i"
            elif self.imaginaire < 0:
                return f"{self.reel}-{abs(self.imaginaire)}i"
            else:
                return str(self.reel)
        elif self.imaginaire != 0:
            return str(self.imaginaire)+"i"
        else:
            return str(self.reel)

    def re(self):
        return self.reel

    def im(self):
        return self.imaginaire

    def mod(self):
        return self.module

    def arg(self):
        return self.argument

    def conj(self):
        return Complexes(self.reel, -self.imaginaire)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Complexes(self.reel*other, self.imaginaire*other)
        elif isinstance(other, Complexes):
            return Complexes(self.reel*other.reel - self.imaginaire*other.imaginaire, self.reel*other.imaginaire + self.imaginaire*other.reel)
        else:
            raise TypeError("unsupported operand type(s) for *: ", type(other), " and 'Complexes'")

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Complexes(self.reel+other, self.imaginaire)
        elif isinstance(other, Complexes):
            return Complexes(self.reel+other.reel, self.imaginaire+other.imaginaire)
        else:
            raise TypeError("unsupported operand type(s) for +: ", type(other), " and 'Complexes'")

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Complexes(self.reel-other, self.imaginaire)
        elif isinstance(other, Complexes):
            return Complexes(self.reel-other.reel, self.imaginaire - other.imaginaire)
        else:
            raise TypeError("unsupported operand type(s) for -: ", type(other), " and 'Complexes'")

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __rsub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Complexes(-self.reel+other, -self.imaginaire)
        elif isinstance(other, Complexes):
            return Complexes(-self.reel+other.reel, -self.imaginaire + other.imaginaire)
        else:
            raise TypeError("unsupported operand type(s) for -: ", type(other), " and 'Complexes'")

    def __neg__(self):
        return Complexes(-self.reel, -self.imaginaire)
    
    def __pow__(self, other):
        return puissance(self, other)

    def __rpow__(self, other):
        print(self.im(), self.re(), other)
        print(log(other)*self.imaginaire, cos(log(other)*self.imaginaire))
        print(puissance(other, self.reel), other**self.reel)
        re = cos(log(other)*self.imaginaire)*puissance(other, self.reel)
        im = sin(log(other)*self.imaginaire)*puissance(other, self.reel)
        if im != 0:
            return Complexes(re, im)
        else:
            return re


class Arbre:
    def __init__(self, val, fg=None, fd=None):
        self.v = val
        self.fg = fg
        self.fd = fd
    def __repr__(self) -> str:
        return f"{self.v} ; {self.fg} ; {self.fd}"


def lire_arbre_calcul(arbre):
    if arbre.v == "*":
        return lire_arbre_calcul(arbre.fg) * lire_arbre_calcul(arbre.fd)
    elif arbre.v == "+":
        return lire_arbre_calcul(arbre.fg) + lire_arbre_calcul(arbre.fd)
    elif arbre.v == "/":
        return lire_arbre_calcul(arbre.fg) / lire_arbre_calcul(arbre.fd)
    elif arbre.v == "-":
        return lire_arbre_calcul(arbre.fg) - lire_arbre_calcul(arbre.fd)
    elif arbre.v == "^":
        return lire_arbre_calcul(arbre.fg) ** lire_arbre_calcul(arbre.fd)
    elif arbre.v == "!":
        return factorielle(lire_arbre_calcul(arbre.fg))
    elif arbre.v == "i":
        return Complexes(0, 1)
    elif arbre.v == "e":
        return e
    elif arbre.v == "pi":
        return pi
    else:
        return int(arbre.v)


def Shuntingyard(calcul: str):
    calcul = rajoute_op(calcul)
    res = []
    operators = []
    i = 0
    while len(calcul) > i:
        if calcul[i] in "+-":
            if len(operators) == 0:
                operators.append(calcul[i])
            else:
                for j in range(len(operators)-1, -1, -1):
                    res.append(operators[j])
                operators = [calcul[i]]
            i += 1
        elif calcul[i] in "*/^":
            operators.append(calcul[i])
            i += 1
        elif calcul[i] == "(":
            temp = ""
            i += 1
            v = 1
            while v > 0:
                temp += calcul[i]
                i += 1
                if calcul[i] == ")":
                    v -= 1
                if calcul[i] == "(":
                    v += 1
            temp = Shuntingyard(temp)
            for j in range(len(temp)):
                res.append(temp[j])
            i += 1
        elif calcul[i] == "!":
            res.append("!")
            i += 1
        else:
            temp = ""
            while i < len(calcul) and calcul[i] not in "*+/-^!":
                temp += calcul[i]
                i += 1
            res.append(temp)
    for i in range(len(operators)-1, -1, -1):
        res.append(operators[i])
    return res


def rajoute_op(calcul):
    i = 0
    while i < len(calcul):
        if not calcul[i].isnumeric() and calcul[i] not in "*/-+^)!":
            if calcul[i:i+4] in ["cos(", "sin(", "tan(", "log(", "abs(", "mod(", "arg("] \
                or calcul[i:i+3] == "ln(" or calcul[i:i+5] in ["sinh(", "cosh(", "tanh(", "sqrt(", "conj("] \
                    or calcul[i:i+7] in ["arccos(", "arcsin(", "arctan("]:
                while calcul[i] != ")":
                    i += 1
            elif calcul[i-1] not in '*/-+^(' and i > 0 and not (calcul[i] == "i" and calcul[i-1] == "p"):
                calcul = calcul[:i] + "*" + calcul[i:]
            elif calcul[i].isalpha() and i+1 < len(calcul)-1 and calcul[i+1] not in "*-/+^)" and not calcul[i+1].isalpha():
                calcul = calcul[:i+1] + "*" + calcul[i+1:]
        i += 1
    return calcul


def puissance(x, n):
    if int(n) == n:
        n = int(n)
    if n == 0:
        return 1
    if isinstance(n, float):
        return puissance(x, int(n)) * e**(log(x)/(1/(n-int(n))))
    elif n < 0:
        return 1/puissance(x, -n)
    elif isinstance(n, int):
        v = 1
        for i in range(n):
            v *= x
        return v


def factorielle(n):
    if n < 0:
        raise ValueError("factorielle d'un nombre négatif est indéfini")
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorielle(n-1)


def npitotree(calcul):
    if len(calcul) == 0:
        return None
    if calcul[-1] in "*+/-^":
        a = Arbre(calcul[-1])
        if calcul[-2] in "*+/-^!":
            a.fd = npitotree(calcul[:-1])
            c = 0
            i = -2
            while c < 3:
                i -= 1
                if calcul[i] not in "*+/-^!":
                    c += 1
                else:
                    c -= 1
            a.fg = Arbre(calcul[i])
        elif calcul[-3] in "*+/-":
            a.fd = Arbre(calcul[-2])
            a.fg = npitotree(calcul[:-2])
        else:
            a.fd = Arbre(calcul[-2])
            a.fg = Arbre(calcul[-3])
    elif calcul[-1] == "!":
        if calcul[-2] not in "*+/-!":
            return Arbre("!", Arbre(calcul[-2]))
        else:
            return(Arbre("!", npitotree(calcul[:-1])))
    return a


def evaluate(ligne):
    npi = Shuntingyard(ligne)
    print(npi)
    arbre = npitotree(npi)
    return lire_arbre_calcul(arbre)


print(evaluate("(2+3)!"))
