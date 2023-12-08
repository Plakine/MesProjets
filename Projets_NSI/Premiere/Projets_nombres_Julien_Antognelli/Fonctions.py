'''
Projet : Ecriture des nombres
Type : Scolaire
Auteur : Julien Antognelli
Date : Octobre 2022
'''
from math import nan


# Binaire vers décimal
def bintodec(n: str) -> int:
    """
    Prends un nombre binaire n et le convertit en base 10
    """
    for i in n:
        if i not in ["0", "1"]:
            raise ValueError("Conversion\
                              bin-déc -> l'entrée n'est pas en base 2")

    # Suppression de la convention d'écriture des nombres binaires
    n = n.lstrip("0b")

    res = 0
    # Boucle de conversion
    for i in range(1, len(n)+1):
        res += int(n[-i])*(2**(i-1))

    return res


# Decimal vers binaire
def dectobin(n: int) -> str:
    """
    Prends un nombre décimal n et le convertit en base 2
    """
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Nombre non décimal")

    result = ""

    # On ajoute n modulo 2 au résultat et on divise n par 2
    while n != 0:
        result = str(n % (2)) + result
        n = n//2
    return result


# Hexadécimal vers décimal
def hextodec(n: str) -> int:
    """
    Prends un nombre hexadécimal n
    et le convertit en base 10
    """
    # Dictionnaire de la base
    n = n.upper()
    hexa = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15
            }
    res = 0
    try:
        for i in range(len(n)):
            res += ((hexa.get(n[-i-1]))*(16**i))
        return (res)
    except KeyError:
        raise ValueError('Nombre non hexadécimal')


# Décimal vers Hexadécimal
def dectohex(n: int) -> str:
    """
    prends un nombre décimal et le convertie en base 16
    """
    try:
        n = int(n)
    except ValueError:
        raise ValueError("Nombre non décimal")
    # Dictionnaire de la base
    hexa = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "A",
            11: "B",
            12: "C",
            13: "D",
            14: "E",
            15: "F"
            }
    result = ""
    while n != 0:
        result = str(hexa.get(n % (16))) + result
        n = n//16
    return result


# Hexadécimal vers binaire
def hextobin(n: str) -> str:
    """
    prends en entrée un nombre n en base 16
    et le renvoie en base 2"""
    n = n.upper()
    # Dictionnaire d'équivalence hexa binaire
    dictbin = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    # On remplace directement par la valeur du dictionnaire
    res = ""
    try:
        for i in n:
            res += dictbin.get(i)
        return res
    except KeyError:
        raise ValueError('nombre non hexadécimal')


# Binaire vers Hexadécimal
def bintohex(n: str) -> str:
    # On vérifies que n est en base 2
    for i in n:
        if i not in ["0", "1"]:
            raise ValueError("Nombre non binaire")
    # On rajoute des 0 pour obtenir des paquets de 4
    while len(n) % 4 != 0:
        n = "0"+n
    # Dictionnaire Binaire : Hexa
    dictbin = {
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }
    res = ""

    # On récupère le binaire par morceaux de 4 bits
    # Qu'on remplace par l'équivalence en base 16
    try:
        for i in range(len(n)//4):
            res += dictbin.get(n[4*i:4*(i+1)])
        return res
    except KeyError:
        # Test redondant avec celui au dessus
        raise ValueError("nombre non binaire")


# Convertisseur d'une base vers une autre
def b1b2(num1: str, b1: int, b2: int):
    """
    Prends un entrée une chaine de charactère représentant
    un nombre dans une base compris entre 2 et 35"""
    try:
        dicto = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15,
            "G": 16,
            "H": 17,
            "I": 18,
            "J": 19,
            "K": 20,
            "L": 21,
            "M": 22,
            "N": 23,
            "O": 24,
            "P": 25,
            "Q": 26,
            "R": 27,
            "S": 28,
            "T": 29,
            "U": 30,
            "V": 31,
            "w": 32,
            "x": 33,
            "Y": 34,
            "Z": 35
        }
        if b1 <= 1 or b1 >= 36:
            raise ValueError("Le paramètre b1 n'est pas inclus dans [1;36]")
        if b2 <= 1 or b2 >= 36:
            raise ValueError("Le paramètre b2 n'est pas inclus dans [1;36]")
        n = 0
        num1 = str(num1)
        # conversion vers base 10
        for i in range(len(num1)):
            n += (dicto.get(num1[-i-1])*(b1**i))
        res = ""
        # conversion vers la base b2
        while n > 0:
            res = list(dicto.keys())[list(dicto.values()).index(n % b2)] + res
            n = n//b2
        return res
    except TypeError:
        raise ValueError("Le paramètre num1 ne représente\
                           pas un nombre dans une base supportée")


# Additionneur bits quelconque
def addany(num1: str, num2: str) -> str:
    """
    additione deux nombres binaires non signées de n'importe quelle taille
    """
    # On vérifies que num1 et num2 sont binaires
    for i in num1:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num1 n'est\
                              pas un nombre non binaire")
    for i in num2:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num2 n'est\
                              pas un nombre non binaire")
    # On ralonge les variables pour qu'elles soient de même taille
    if len(num1) >= len(num2):
        while len(num2) != len(num1):
            num2 = "0"+num2
    else:
        while len(num1) != len(num2):
            num1 = "0"+num1
    retenue = 0
    res = ""
    for i in range(len(num1)):
        if int(num1[-i-1])+int(num2[-i-1])+int(retenue) in [1, 3]:
            res = "1"+res
        else:
            "0"+res
        if int(num1[-i-1])+int(num2[-i-1])+int(retenue) > 1:
            retenue = 1
        else:
            retenue = 0
    # S'il reste une retenue on rajoute un "1"
    if retenue == 1:
        res = "1"+res
    return res


# Additionneur à nombre de bits fixe
def addfix(num1: str, num2: str, lenmax: int) -> str:
    """
    additionne les entrées num1 et num2 jusqu'au lenmax-ieme bit
    """
    for i in num1:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num1 n'est\
                              pas un nombre non binaire")
    for i in num2:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num2 n'est\
                              pas un nombre non binaire")
    assert isinstance(lenmax, int), ("le paramètre lenmax n'est pas un entier")
    while len(num1) < lenmax:
        num1 = "0"+num1
    while len(num2) < lenmax:
        num2 = "0"+num2
    retenue = 0
    res = ""
    for i in range(lenmax):
        if int(num1[-i-1])+int(num2[-i-1])+int(retenue) in [1, 3]:
            res = "1"+res
        else:
            res = "0"+res
        if int(num1[-i-1])+int(num2[-i-1])+int(retenue) > 1:
            retenue = 1
        else:
            retenue = 0
    return res


# Soustracteur à nombre de bit quelconque
def subany(num1: str, num2: str) -> str:
    """
    réalise une soustraction sur deux nombres binaires num1 et num2
    et renvoie num1-num2
    """
    for i in num1:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num1 n'est\
                              pas un nombre non binaire")
    for i in num2:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num2 n'est\
                              pas un nombre non binaire")
    # on rallonge les nombres pour qui soient de même longueur
    while len(num1) != len(num2):
        if len(num1) > len(num2):
            num2 = "0"+num2
        else:
            num1 = "0"+num1
    res = ""
    retenue = 0
    for i in range(len(num1)):
        if int(num1[-i-1])-(int(num2[-i-1])+retenue) in [1, -1, -3]:
            res = "1"+res
        elif int(num1[-i-1])-(int(num2[-i-1])+retenue) in [0, -2]:
            res = "0"+res
        if int(num1[-i-1])-(int(num2[-i-1])+retenue) < 0:
            retenue = 1
        else:
            retenue = 0
    return res


# soustracteur à nombre de bits fixe
def subfix(num1: str, num2: str, lenmax: int) -> str:
    """
    prends en entrée deux nombres binaires num1 et num2
    ainsi qu'un entier lenmax
    et réalise la soustraction num1-num2 jusqu'au lenmaxieme bit"""
    for i in num1:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num1 n'est\
                              pas un nombre non binaire")
    for i in num2:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num2 n'est\
                              pas un nombre non binaire")
    assert isinstance(lenmax, int), ("le paramètre lenmax n'est pas un entier")

    # on rallonge les nombres pour qui soient de même longueur
    while len(num1) != lenmax:
        if len(num1) < lenmax:
            num1 = "0"+num1
        else:
            num1 = num1[1:]
    while len(num2) != lenmax:
        if len(num2) < lenmax:
            num2 = "0"+num2
        else:
            num2 = num2[1:]

    res = ""
    retenue = 0
    for i in range(lenmax):
        if int(num1[-i-1])-(int(num2[-i-1])+retenue) in [1, -1]:
            res = "1"+res
        elif int(num1[-i-1])-(int(num2[-i-1])+retenue) in [0, -2]:
            res = "0"+res
        if int(num1[-i-1])-(int(num2[-i-1])+retenue) < 0:
            retenue = 1
        else:
            retenue = 0
    return res


# multiplicateur à nombre de bit quelconque
def multipleany(num1: str, num2: str) -> str:
    """
    renvoie le résultat de la multiplication de deux entiers en base 2
    """
    for i in num1:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num1 n'est\
                              pas un nombre non binaire")
    for i in num2:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num2 n'est\
                              pas un nombre non binaire")

    presumlist = []
    res_act = ""

    for i in range(len(num1)):
        for j in range(len(num2)):
            if (int(num1[-i-1]) and int(num2[-j-1])) == 1:
                res_act = "1"+res_act
            else:
                res_act = "0"+res_act
        presumlist.append(res_act)
        res_act = "0"*(i+1)
        # On récupère une liste (presumlist) de binaires à additionner
    # On additionne tout
    while len(presumlist) != 1:
        presumlist.append(addany(presumlist[0], presumlist[1]))
        presumlist.pop(0)
        presumlist.pop(0)
    res = presumlist[0].lstrip("0")
    return res


# multiplicateur à nombre de bit fixe
def multiplefix(num1: str, num2: str, lenmax: int) -> str:
    """
    renvoie le résultat de la multiplication de deux entiers en base 2
    jusqu'au lenmaxieme bit
    """
    for i in num1:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num1 n'est\
                              pas un nombre non binaire")
    for i in num2:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num2 n'est\
                              pas un nombre non binaire")
    assert isinstance(lenmax, int), ("le paramètre lenmax n'est pas un entier")
    # on mets tout à la longueur demandé
    while len(num1) < lenmax:
        num1 = "0"+num1
    while len(num2) < lenmax:
        num2 = "0"+num2
    presumlist = []
    crntres = ""
    # On multiplie
    for i in range(len(num1)):
        for j in range(len(num2)):
            if (int(num1[-i-1]) and int(num2[-j-1])) == 1:
                crntres = "1"+crntres
            else:
                crntres = "0"+crntres
        presumlist.append(crntres)
        crntres = "0"*(i+1)
    # On additionne
    while len(presumlist) != 1:
        presumlist.append(addany(presumlist[0], presumlist[1]))
        presumlist.pop(0)
        presumlist.pop(0)
    res = presumlist[0]
    # On raccourci pour la bonne longueur
    if len(res) > lenmax:
        while len(res) != lenmax:
            res = res[1:]
    elif len(res) < lenmax:
        while len(res) != lenmax:
            res = "0"+res
    return res


# convertisseur décimal complément à 2 avec choix du nombre de bit
def deccomp2fix(num1: int, precision: int) -> str:
    # On vérifie que les entrées sont du bon type
    assert isinstance(num1, int), ("le paramètre num1 n'est pas un entier")
    assert isinstance(precision, int), ("le paramètre précision\
                                         n'est pas un entier")
    # On récupère la forme binaire
    n = dectobin(num1)
    # On l'ajuste pour la precision
    while len(n) != precision:
        if len(n) < precision:
            n = "0"+n
        elif len(n) > precision:
            n = n[1:]
    res = ""
    # On inverse les nombres
    for i in n:
        res += "1" if i == "0" else "0"
    # On ajoute 1
    while "1" in addfix(n, res, len(n)):
        res = addfix(res, "1", len(res))
    return res


# convertisseur décimal complément à 2 sans choix du nombre de bits
def deccomp2any(num1: int) -> str:
    assert isinstance(num1, int), ("le paramètre num1 n'est pas un entier")
    n = dectobin(num1)
    res = ""
    for i in n:
        res += "1" if i == "0" else "0"
    while "1" in addfix(n, res, len(n)):
        res = addfix(res, "1", len(res))
    return res


# convertisseur complément à 2  -> décimal avec choix du nombre de bit
def comp2decfix(num1: str, lenmax: int) -> int:
    # On vérfie que les entrées sont du bon type
    assert isinstance(lenmax, int), ("Le paramètre lenmax n'est pas un entier")
    assert isinstance(num1, str), ("Le paramètre num1 n'est\
                                    pas un nombre binaire")
    for i in num1:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num1 n'est\
                              pas un nombre non binaire")
    # On ajuste à la précision
    while len(num1) != lenmax:
        if len(num1) > lenmax:
            num1 = num1[:1]
        else:
            num1 = "0"+num1
    res = ""
    # On inverse et on additionne 1
    for i in num1:
        res += "1" if i == "0" else "0"
    res = addfix(res, "1", len(res))
    # On renvoie le decimal
    return bintodec(res)


# convertisseur complément à 2  -> décimal sans choix du nombre de bits
def comp2decany(num1: str) -> int:
    assert isinstance(num1, str), ("Le paramètre num1 n'est\
                                    pas un nombre binaire")
    for i in num1:
        if i != "0" or i != "1":
            raise ValueError("le paramètre num1 n'est\
                              pas un nombre non binaire")
    res = ""
    for i in num1:
        res += "1" if i == "0" else "0"
    res = addfix(res, "1", len(res))
    return bintodec(res)


# convertisseur décimal flottant
def dectofloatany(n: float) -> str:
    # On vérifie le type de l'entrée
    assert isinstance(n, float), ("Le paramètre n n'est pas un flottant")
    # On récupère le binaire de la partie entiere de n
    entiern = dectobin(int(n))
    # On récupère la partie décimale de n
    decimal = str(n)
    try:
        while decimal[0] != ".":
            decimal = decimal[1:]
    # Si n n'est pas un float
    except IndexError:
        raise (TypeError("Le paramètre n n'est pas un flottant"))
    decimal = int(decimal[1:])
    # Décalage pour éviter d'avoir des problèmes d'arrondi
    decalage = len(str(decimal))
    res = entiern+","
    # On multiplie par 2 si on dépasse la puissance de 10 choisie au dessus
    # on met 1 sinon 0
    while decimal != 0 and len(res) < 64:
        decimal *= 2
        if decimal >= 1*10**decalage:
            res += "1"
            decimal -= 1*10**decalage
        else:
            res += "0"
    return res


# convertisseur decimal flottant sans choix
def dectofloatfix(n: float, precision: int) -> str:
    assert isinstance(n, float), "Le paramètre n n'est pas un flottant"
    assert isinstance(precision, int), "Le paramètre precision\
          n'est pas un entier"
    entiern = dectobin(int(n))
    decimal = str(n)
    while decimal[0] != ".":
        decimal = decimal[1:]
    decimal = int(decimal[1:])
    decalage = len(str(decimal))
    res = entiern+","

    while decimal != 0 and len(res) < precision:
        decimal *= 2
        if decimal >= 1*10**decalage:
            res += "1"
            decimal -= 1*10**decalage
        else:
            res += "0"

    return res


# convertisseur flottant decimal sans choix
def floattodecany(n: str) -> int:
    # On vérifie le type de l'entrée
    try:
        if "," not in n:
            raise (TypeError)
        for i in n:
            if i not in ["0", '1', ","]:
                raise (TypeError)
    except TypeError:
        return ("le param n n'est pas une chaine de charactères représentant\
                 un flottant")
    # On récupère la partie entière
    entier = ""
    while n[0] != ",":
        entier += n[0]
        n = n[1:]
    n = n[1:]
    # On récupère la forme decimale de l'entier
    entier = bintodec(entier)
    # on récupère la virgule
    virgulein = n
    virguleout = 0
    # On multiplie chaque chiffre de la virgule par
    #  2 puissance -(la distance de la virgule)
    for i in range(len(virgulein)):
        virguleout += int(virgulein[i])*2**(-i-1)
    return (entier+virguleout)


# convertisseur flottant vers décimal avec choix
def floattodecfix(n: str, precision: int) -> int:
    assert isinstance(n, str), "le paramètre n n'est pas\
         une chaine de charactères"
    assert isinstance(precision, str), "le paramètre precision\
          n'est pas un entier"
    if "," not in n:
        raise (TypeError)
    for i in n:
        if i not in ["0", '1', ","]:
            raise (TypeError)
    entier = ""
    while n[0] != ",":
        entier += n[0]
        n = n[1:]
    n = n[1:]
    virgulein = n
    entier = bintodec(entier)
    virguleout = 0
    for i in range(len(virgulein)):
        if len(str(virguleout)) < precision:
            virguleout += int(virgulein[i])*2**(-i-1)
        else:
            break
    return (entier+virguleout)


# Convertisseur décimal ieee754 précision au choix et sans choix
def dectoieee754(n: int, precision="double"):
    try:
        # On récupère les spécificitées en fonction de la précision
        if precision.lower() != "double" and precision.lower() != "simple":
            raise ValueError("precision isn't 'double' or 'simple'")
        decal = 1023 if precision.lower() == "double" else 127
        mantisselen = 52 if precision.lower() == "double" else 23
        exposantlen = 11 if precision.lower() == "double" else 8
        fullresult = ""

        # Cas particulier
        # Zéros
        if str(n) == "-0":
            return "1"+" "+"0"*exposantlen+" "+"0"*mantisselen
        elif str(n) == "+0":
            return "0"+" "+"0"*exposantlen+" "+"0"*mantisselen
        elif str(n) == "nan":
            return "0"+" "+"1"*exposantlen+" "+"1"*mantisselen
        elif n == float("-inf"):
            return "1"+" "+"1"*exposantlen+" "+"0"*mantisselen
        elif n == float("inf"):
            return "0"+" "+"1"*exposantlen+" "+"0"*mantisselen
        try:
            n = float(n)
        except ValueError:
            return ValueError("not int")
        # Le signe
        if n < 0:
            fullresult = "1 "
        else:
            fullresult = "0 "
        # On différencie les différentes formes de n à utiliser
        n = abs(n)
        fulln = int(n)
        result = ""
        # Cas particulier du 0
        if n == 0:
            return ("0"+" "+"0"*exposantlen+" "+"0"*mantisselen)
        # Le nombre
        while fulln != 0:
            result = str(fulln % (2)) + result
            fulln = fulln//2
        if len(result) > mantisselen+1:
            raise (OverflowError)
        # L'exposant
        result = result[1:]
        exposant = (dectobin(decal+len(result)))
        while len(exposant) < exposantlen:
            exposant = "0"+exposant
        # La virgule
        floatn = dectofloatany(n)
        if floatn[-1] != ",":
            for i in floatn:
                if i != ",":
                    floatn = floatn[1:]
                else:
                    break
            result += (floatn[1:])
        # Le tout
        result += "0"*(mantisselen-len(result))
        fullresult += (exposant+" "+result)
        return fullresult
    except OverflowError:
        return ("Num too big")


# Convertisseur ieee754 vers decimal
def ieeetodec(n: str, precision="double"):
    # On vérifies le type
    for i in n:
        if i not in ["1", "0", " "]:
            raise TypeError("Not float (IEEE754)")
    # On récupère les spécificitées en fonction de la précision
    if precision.lower() == "simple":
        decal = 127
        expolen = 8
    elif precision.lower() == "double":
        decal = 1023
        expolen = 11
    # Si précision non valable
    else:
        return "precision (arg 2) should be 'double' or 'simple' "
    # On enlève les espaces de lecture
    n = n.replace(" ", "")

    # On récupère l'exposant
    exposant = n[1:expolen+1]
    # On récupère le reste
    mantisse = n[expolen+1:]
    mantissefin = "1"
    # Cas particuliers
    if "0" not in exposant:
        if "1" not in mantisse:
            if n[0] == "0":
                return float("inf")
            else:
                return float('-inf')
        else:
            return nan
    if "1" not in exposant and "1" not in mantisse:
        if n[0] == "1":
            return -0
        else:
            return +0
    # On récupère la forme décimal de l'exposant
    # et on l'ajuste pour la précision
    exposant = bintodec(exposant)-decal

    # On décale la virgule tant que l'exposant >1
    while exposant >= 1 and len(mantisse) > 0:
        mantissefin = mantissefin + mantisse[0]
        mantisse = mantisse[1:]
        exposant -= 1
    # On s'occupe de la partie à virgule
    if "1" in mantisse:
        mantissefin += ","
        while "1" in mantisse and len(mantisse) > 0:
            mantissefin += mantisse[0]
            mantisse = mantisse[1:]
    # On convertie en décimal
        res = floattodecany(mantissefin)
    else:
        res = bintodec(mantissefin)
    # On rajoute le signe si besoin
    if n[0] == "1":
        res = -res
    return res


# compare deux nombres binaires,
# n1>n2 -> 1
# n2>n1 -> 2
# n1==n2-> 3
def comparebin(n1: str, n2: str) -> int:
    # On vérifie les types des entrées
    for i, j in zip(n1, n2):
        if i not in ["0", "1"] or j not in ["0", "1"]:
            raise ValueError("Nombre non binaire")
    # On enlève les 0 inutiles
    n1 = n1.lstrip("0")
    n2 = n2.lstrip("0")

    # Le plus long est plus grand
    if len(n1) > len(n2):
        return 1
    elif len(n2) > len(n1):
        return 2
    # Le premier qui a un 0 est plus petit
    for i in range(len(n1)):
        if n1[i] != n2[i]:
            if n1[i] == "1":
                return 1
            elif n2[i] == "1":
                return 2
    # égalité
    return 3


# Additione deux nombres flottants (ieee754) avec double précision
def addieee754doublepre(n1: (str or int), n2: (str or int)) -> str:
    # On vérifie que les nombres soient du bon type (string ou int)
    if isinstance(n1, int):
        n1 = int(n1)
        n1 = dectoieee754(n1)
    if isinstance(n2, int):
        n2 = int(n2)
        n2 = dectoieee754(n2)
    # Cas particulier
        # nan
    if n1 == "0 11111111111\
          1111111111111111111111111111111111111111111111111111":
        return nan
        # infini
    elif n1 == "1 11111111111\
         0000000000000000000000000000000000000000000000000000":
        return float('-inf')
    elif n1 == "0 11111111111\
         0000000000000000000000000000000000000000000000000000":
        return float('+inf')
    elif n2 == "0 11111111111\
         1111111111111111111111111111111111111111111111111111":
        return nan
    elif n2 == "1 11111111111\
         0000000000000000000000000000000000000000000000000000":
        return float('-inf')
    elif n2 == "0 11111111111\
         0000000000000000000000000000000000000000000000000000":
        return float('+inf')
    # On vérifie que les nombres
    try:
        if len(n1) != len(n2):
            raise (TypeError)
    except TypeError:
        return TypeError("numbers aren't the same precision: should be double")
    while " " in n1 or " " in n2:
        n1 = n1.replace(" ", "")
        n2 = n2.replace(" ", "")
    # On récupère l'exponant des nombres
    expon1 = n1[1:12]
    expon2 = n2[1:12]
    if n1[0] != n2[0]:
        return "this doesn't support substraction"
    # On récupère la mantisse des nombres
    mantissa1 = "1"+n1[12:]
    mantissa2 = "1"+n2[12:]
    flag = False

    # On modifie les nombres pour avoir le même exposant
    if comparebin(expon1, expon2) == 1:
        while comparebin(expon1, expon2) != 3:
            if flag:
                expon2 = addfix(expon2, "1", 11)
                mantissa2 = "0"+mantissa2
                mantissa2 = mantissa2[:-1]
            else:
                flag = True
    elif comparebin(expon1, expon2) == 2:
        while comparebin(expon1, expon2) != 3:
            if flag:
                expon1 = addfix(expon1, "1", 11)
                mantissa1 = "0"+mantissa1
                mantissa1 = mantissa1[:-1]
            else:
                flag = True
    # Comme expon1 = Expon2 on pourrait remplacer expon1 par expon2
    exponantfinal = expon1
    # On ajoute
    mantissefinale = addany(mantissa1, mantissa2)
    # On elnève le premier nombre comme on a rajouter les "1"
    mantissefinale = mantissefinale[1:]
    # Si le nombre est trop grand
    while len(mantissefinale) > 52:
        mantissefinale = mantissefinale[:-1]
        exponantfinal = addfix(expon1, "1", 11)
    # Les signes différents ne sont pas accepté
    signefinal = n1[0]
    return (signefinal+" "+exponantfinal+" "+mantissefinale)


# Soustrait deux nombres flottants (ieee754) avec double précision
# Fonctionne de la même façon que la fonction addiee754doublepre()
# Mais on soustrait à la place d'additionner les mantisses
def subieedoublepré(n1, n2):
    # On vérifie que les nombres soient du bon type (string ou int)
    if isinstance(n1, int):
        n1 = int(n1)
        n1 = dectoieee754(n1)
    if isinstance(n2, int):
        n2 = int(n2)
        n2 = dectoieee754(n2)
    # Cas particulier
    if n1 == "0 11111111111\
         1111111111111111111111111111111111111111111111111111":
        return nan
    elif n1 == "1 11111111111\
         0000000000000000000000000000000000000000000000000000":
        return float('-inf')
    elif n1 == "0 11111111111\
         0000000000000000000000000000000000000000000000000000":
        return float('+inf')
    elif n2 == "0 11111111111\
         1111111111111111111111111111111111111111111111111111":
        return nan
    elif n2 == "1 11111111111\
         0000000000000000000000000000000000000000000000000000":
        return float('-inf')
    elif n2 == "0 11111111111\
         0000000000000000000000000000000000000000000000000000":
        return float('+inf')
    # On vérifie que les nombres
    try:
        if len(n1) != len(n2):
            raise (TypeError)
    except TypeError:
        return TypeError("numbers aren't the same precision: should be double")
    while " " in n1 or " " in n2:
        n1 = n1.replace(" ", "")
        n2 = n2.replace(" ", "")
    # On récupère l'exponant des nombres
    expon1 = n1[1:12]
    expon2 = n2[1:12]
    if n1[0] != n2[0]:
        return "this doesn't support substraction"
    # On récupère la mantisse des nombres
    mantissa1 = "1"+n1[12:]
    mantissa2 = "1"+n2[12:]
    flag = False
    if comparebin(expon1, expon2) == 1:
        while comparebin(expon1, expon2) != 3:
            if flag:
                expon2 = addfix(expon2, "1", 11)
                mantissa2 = "0"+mantissa2
                mantissa2 = mantissa2[:-1]
            else:
                flag = True
    elif comparebin(expon1, expon2) == 2:
        while comparebin(expon1, expon2) != 3:
            if flag:
                expon1 = addfix(expon1, "1", 11)
                mantissa1 = "0"+mantissa1
                mantissa1 = mantissa1[:-1]
            else:
                flag = True
    exponantfinal = expon1
    print(mantissa1)
    print(mantissa2)
    mantissefinale = subany(mantissa1, mantissa2)
    mantissefinale = mantissefinale[1:]
    flag = True
    while mantissefinale[0] != "1" or flag:
        mantissefinale = mantissefinale[1:]+"0"
        exponantfinal = subfix(exponantfinal, "1", 11)
        flag = False
    while len(mantissefinale) > 52:
        mantissefinale = mantissefinale[:-1]
        exponantfinal = subfix(exponantfinal, "1", 11)
    signefinal = n1[0]
    return (signefinal+" "+exponantfinal+" "+mantissefinale)
