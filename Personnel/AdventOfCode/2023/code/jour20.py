data = open("data/jour20.txt").read().splitlines()

def innit(dictionnaire):
    output = []
    for machine in dictionnaire:
        for dest in dictionnaire[machine][0]:
            if dest in dictionnaire.keys():
                if dictionnaire[dest][-1] == 1:
                    dictionnaire[dest][1][machine] = 1 
            else:
                output.append(dest)
    return output

def sendsignal(dictionnaire, signal, output):
    source = signal[0]
    force = signal[1]
    nouveaux_signaux = []
    res1 = 0
    res2 = 0
    for destinations in dictionnaire[source][0]:
        if destinations in output:
            pass
        elif dictionnaire[destinations][-1] == 0:
            if force == 1:
                dictionnaire[destinations][-2] = (dictionnaire[destinations][-2]+1)%2
                nouveaux_signaux.append((destinations, dictionnaire[destinations][-2]+1))               
        elif dictionnaire[destinations][-1] == 2:
            nouveaux_signaux.append((destinations, 1))
        elif dictionnaire[destinations][-1] == 1:
            dictionnaire[destinations][1][source] = force
            if 1 not in dictionnaire[destinations][1].values():
                nouveaux_signaux.append((destinations, 1))
            else:
                nouveaux_signaux.append((destinations, 2))
    return nouveaux_signaux, (res1, res2)



def partie1():
    somme1 = 0
    somme2 = 0
    signal_sent = []
    beginning = []
    dictionnaire = {"button":[["broadcaster"], 0, 4]}
    for line in data:
        if line[0] == "b":
            # Broadcast
            # (Connections, placeholder, type)
            value = "broadcaster"
            destina = line[1:].split(" -> ")[1].split(", ")
            dictionnaire[value] = [destina, 0, 2]
        elif line[0] == "%":
            value = line[1:].split(" -> ")[0]
            # (Connections, On/Off, type)    
            dictionnaire[value] = [line[1:].split(" -> ")[1].split(", "), 0, 0]
        elif line[0] == "&":
            value = line[1:].split(" -> ")[0]
            # (Connections, signal enregistré, type)    
            dictionnaire[value] = [line[1:].split(" -> ")[1].split(", "), {}, 1]
    output = innit(dictionnaire)
    for i in range(1000):
        signal_sent = [("button", 1)]
        while len(signal_sent) > 0:
            nsignaux = sendsignal(dictionnaire, signal_sent[0], output)[0]
            if signal_sent[0][-1] == 1:
                somme1 += len(dictionnaire[signal_sent[0][0]][0])
            if signal_sent[0][-1] == 2:
                somme2 += len(dictionnaire[signal_sent[0][0]][0])
            signal_sent += nsignaux
            signal_sent.pop(0)
    return somme1*somme2

from math import lcm

def partie2():
    signal_sent = []
    dictionnaire = {"button":[["broadcaster"], 0, 4]}
    for line in data:
        if line[0] == "b":
            # Broadcast
            # (Connections, placeholder, type)
            value = "broadcaster"
            destina = line[1:].split(" -> ")[1].split(", ")
            dictionnaire[value] = [destina, 0, 2]
        elif line[0] == "%":
            value = line[1:].split(" -> ")[0]
            # (Connections, On/Off, type)    
            dictionnaire[value] = [line[1:].split(" -> ")[1].split(", "), 0, 0]
        elif line[0] == "&":
            value = line[1:].split(" -> ")[0]
            # (Connections, signal enregistré, type)
            dictionnaire[value] = [line[1:].split(" -> ")[1].split(", "), {}, 1]
    output = innit(dictionnaire)
    i = 0
    flag1 = True
    flag2 = True
    flag3 = True
    flag4 = True
    numb = []
    while flag1 or flag2 or flag3 or flag4:
        i += 1
        signal_sent = [("button", 1)]
        while len(signal_sent) > 0:
            if flag1 and signal_sent[0] == ("zp", 1):
                flag1 = not flag1
                numb.append(i)
            if flag2 and signal_sent[0] == ("ph", 1):
                flag2 = not flag2
                numb.append(i)
            if flag3 and signal_sent[0] == ("jn", 1):
                flag3 = not flag3
                numb.append(i)
            if flag4 and signal_sent[0] == ("mf", 1):
                flag4 = not flag4
                numb.append(i)
            
            nsignaux = sendsignal(dictionnaire, signal_sent[0], output)[0]
            signal_sent += nsignaux
            signal_sent.pop(0)
    return lcm(*numb)
print(partie1())
print(partie2())