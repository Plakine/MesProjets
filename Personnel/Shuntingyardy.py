"""
Algorithme de Shunting Yard
"""


def Shuntingyard(calcul: str):
    res = []
    operators = []
    i = 0
    while len(calcul) > 0:
        j = i
        temp = ""
        if calcul[i] not in "*+/-":
            while calcul[j] not in "*+-/":
                temp += calcul[j]
                calcul = calcul[1:]
                if j == len(calcul):
                    break
            res.append(temp)
            if len(calcul) == 0:
                break
        else:
            if calcul[i] == "*" or calcul[i] == "/":
                if len(operators) > 0:
                    if operators[-1] != "*" and operators[-1] != "/":
                        operators.append(calcul[i])
                    else:
                        for i in range(len(operators)-1, -1, -1):
                            res.append(operators[i])
                        operators = calcul[i]
            else:
                if len(operators) == 0:
                    operators.append(calcul[i])
                else:
                    for i in range(len(operators)-1, -1, -1):
                        res.append(operators[i])
                    operators = calcul[i]
            calcul = calcul[1:]
    if len(operators) != 0:
        for i in range(len(operators)-1, -1, -1):
            res.append(operators[i])
    return res


def Calculate(shunt: list):
    i = 1
    res = 0
    while i < len(shunt):
        if shunt[i] == "+":
            shunt[i-2] = int(shunt[i-2]) + int(shunt[i-1])
            shunt.pop(i)
            shunt.pop(i-1)
            i = 0
        elif shunt[i] == "-":
            shunt[i-2] = int(shunt[i-2]) - int(shunt[i-1])
            shunt.pop(i)
            shunt.pop(i-1)
            i = 0

        elif shunt[i] == "*":
            shunt[i-2] = int(shunt[i-2]) * int(shunt[i-1])
            shunt.pop(i)
            shunt.pop(i-1)
            i = 0

        elif shunt[i] == "/":
            shunt[i-2] = int(shunt[i-2]) / int(shunt[i-1])
            shunt.pop(i)
            shunt.pop(i-1)
            i = 0
        else:
            i += 1
    res = shunt[0]
    return res


print(Calculate(Shuntingyard("3+2*10-25")))
