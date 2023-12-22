data = open("data/jour19.txt").read().splitlines()
for i in range(len(data)):
    if data[i] == "":
        data1 = data[:i]
        data2 = data[i+1:]
        break

def create_dic(donnes):
    valdic = {}
    for line in donnes:
        nom, lois = line.split("{")
        lois = lois.strip("}").split(",")
        valdic[nom] = lois
    return valdic

def read_values(ligne):
    ligne = ligne.strip("{}").split(",")
    vals = []
    for valeurs in ligne:
        vals.append(int(valeurs.split("=")[1]))
    return vals

def find_nextbal(xmas, rules):
    dicto = {
        "x": xmas[0],
        "m": xmas[1],
        "a": xmas[2],
        "s": xmas[3],
    }
    for rule in rules:
        if ":" not in rule:
            return rule
        else:
            comparison, result = rule.split(":")
            searched_value = dicto[comparison[0]]
            if comparison[1] == ">" and searched_value>int(comparison[2:]):
                return result
            if comparison[1] == "<" and searched_value<int(comparison[2:]):
                return result

            

def partie1(donnes_1, donnes_2):
    somme = 0
    dictionnaire = create_dic(donnes_1)
    for line in donnes_2:
        xmas = read_values(line)
        next_bal = "in"
        while next_bal not in "AR":
            next_bal = find_nextbal(xmas, dictionnaire[next_bal])
        if next_bal == "A":
            somme += sum(xmas)
    return somme

class ranges:
    def __init__(self,x1,x2,m1,m2,a1,a2,s1,s2, nxt) -> None:
        self.x1 = x1
        self.x2 = x2
        self.m1 = m1
        self.m2 = m2
        self.a1 = a1
        self.a2 = a2
        self.s1 = s1
        self.s2 = s2
        self.name = nxt
    def __repr__(self) -> str:
        return f"[{self.x1}, {self.x2},{self.m1},{self.m2},{self.a1},{self.a2},{self.s1},{self.s2},{self.name}]"
    def check_validity(self):
        if self.x2 < self.x1 or self.m2 < self.m1 or self.a2 < self.a1 or self.s2 < self.s1:
            return False
        return True

    def next(self, rules):
        res = []
        if not self.check_validity():
            return []
        for rule in rules:
            if ":" not in rule:
                res.append(ranges(self.x1, self.x2,self.m1, self.m2,self.a1, self.a2, self.s1, self.s2, rule))
            else:
                comparison, result = rule.split(":")
                value = int(comparison[2:])
                if comparison[1] == ">":
                    if comparison[0] == "x" and self.x2 > value:
                        res.append(ranges(max(self.x1, value+1), self.x2,self.m1, self.m2,self.a1, self.a2, self.s1, self.s2, result))
                        self.x2 = value
                    elif comparison[0] == "m" and self.m2 > value:
                        res.append(ranges(self.x1, self.x2,max(self.m1, value+1), self.m2,self.a1, self.a2, self.s1, self.s2, result))
                        self.m2 = value
                    elif comparison[0] == "a" and self.a2 > value:
                        res.append(ranges(self.x1, self.x2,self.m1, self.m2,max(self.a1, value+1), self.a2, self.s1, self.s2, result))
                        self.a2 = value
                    elif comparison[0] == "s" and self.s2 > value:
                        res.append(ranges(self.x1, self.x2,self.m1, self.m2,self.a1, self.a2, max(self.s1, value+1), self.s2, result))
                        self.s2 = value
                elif comparison[1] == "<":
                    if comparison[0] == "x" and self.x1 < value:
                        res.append(ranges(self.x1, min(self.x2,value-1) ,self.m1, self.m2,self.a1, self.a2, self.s1, self.s2, result))
                        self.x1 = value
                    elif comparison[0] == "m"and self.m1 < value:
                        res.append(ranges(self.x1, self.x2,self.m1, min(self.m2,value-1),self.a1, self.a2, self.s1, self.s2, result))
                        self.m1 = value
                    elif comparison[0] == "a"  and self.a1 < value:
                        res.append(ranges(self.x1, self.x2,self.m1, self.m2,self.a1, min(self.a2,value-1), self.s1, self.s2, result))
                        self.a1 = value
                    elif comparison[0] == "s" and self.s1 < value:
                        res.append(ranges(self.x1, self.x2,self.m1, self.m2,self.a1, self.a2, self.s1, min(self.s2, value-1), result))
                        self.s1 = value
        return res



def partie2(donnes_1):
    somme = 0
    dictionnaire = create_dic(donnes_1)
    res = [ranges(1,4000,1,4000,1,4000,1,4000, "in")]
    while len(res) > 0:
        res2 = []
        for rang in res:
            newranges = []
            if rang.name == "A" and rang.check_validity():
                somme += (rang.x2-rang.x1+1)*(rang.m2-rang.m1+1)*(rang.a2-rang.a1+1)*(rang.s2-rang.s1+1)
            elif rang.name not in "AR":
                newranges = rang.next(dictionnaire[rang.name])
            for i in range(len(newranges)):
                res2.append(newranges[i])
        res = [i for i in res2]
    return somme
e1 = partie1(data1, data2)
e2 = partie2(data1)
print("Jour 19: \n  Partie 1:", (e1), "\n  Partie 2:", (e2))
