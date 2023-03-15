'''
Projet : Ecriture des nombres
Julien Antognelli
'''
#Binaire vers décimal
def bintodec(n:str)->int:
    n = n.lstrip("0b") #Dans le cas où le nombre binaire a été généré avec bin()
    res = 0 #Création de la variable que l'on renvoi
    for i in range(1,len(n)+1):  #On itère sur la longueur de n
        res += int(n[-i])*(2**i)/2 #On ajoute au résultat la valeur du 0/1 
    return int(res)

#Decimal vers binaire
def dectobin(n:int)->str: 
    result = "" #Création de la variable que l'on renvoi
    
    #On ajoute le reste (0 ou 1 en str) de n/2 au résultat et on divise n par 2
    while n!=0: 
        result = str(n%(2)) + result
        n = n//2
    return result

#Hexadécimal vers décimal
def hextodec(n:str)->int:
    #Dictionnaire de la base
    n= n.upper()
    hexa = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5,"6":6, "7":7,"8":8,"9":9,"A":10, "B":11,"C":12,"D":13,"E":14,"F":15}
    #on définit notre variable résultat
    res = 0
    #On récupère l'équivalent decimal dans le dictionnaire et on le multiplie par 16^n 
    for i in range(len(n)):
        res+= ((hexa.get(n[-i-1]))*(16**i))
    return(res)

#Décimal vers Hexadécimal
def dectohex(n:int)->str:
    #Dictionnaire de la base
    hexa = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8",9:"9",10:"A", 11:"B",12:"C",13:"D",14:"E",15:"F"}
    #on définit notre variable résultat
    result = ""
    #On récupère l'équivalent hexadécimal dans le dictionnaire et on le divise par 16
    while n!=0:
        result = str(hexa.get(n%(16))) + result
        n = n//16
    return result

#Hexadécimal vers binaire
def hextobin(n:str)->str:
    n=n.upper()
    #Dictionnaire d'équivalence hexa binaire
    dictbin = {
        "0":"0000",
        "1" :"0001",
        "2":"0010",
        "3":"0011",
        "4":"0100",
        "5":"0101",
        "6":"0110",
        "7":"0111",
        "8":"1000",
        "9":"1001",
        "A":"1010",
        "B":"1011",
        "C":"1100",
        "D":"1101",
        "E":"1110",
        "F":"1111",
    } #Dictionnaire 
    #On remplace directement par la valeur du dictionnaire
    res = ""
    for i in n:
        res+=dictbin.get(i)
    return res

#Binaire vers Hexadécimal
def bintohex(n:str)->str:
    while len(n)%4 !=0:
        n = "0"+n
    dictbin = {
        "0000":"0",
        "0001":"1",
        "0010":"2",
        "0011":"3",
        "0100":"4",
        "0101":"5",
        "0110":"6",
        "0111":"7",
        "1000":"8",
        "1001":"9",
        "1010":"A",
        "1011":"B",
        "1100":"C",
        "1101":"D",
        "1110":"E",
        "1111":"F",
    } #Dictionnaire 
    res=""
    #On récupère le binaire par morceaux de 4 bits et on remplace par l'équivalence en hexa
    for i in range(len(n)//4):
        res+=dictbin.get(n[4*i:4*(i+1)])
    return res

#Convertisseur b1 vers b2
def b1b2(num1:str,b1,b2:int):
    dicto={
        "0":0,
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "A":10,
        "B":11,
        "C":12,
        "D":13,
        "E":14,
        "F":15,
        "G":16,
        "H":17,
        "I":18,
        "J":19,
        "K":20,
        "L":21,
        "M":22,
        "N":23,
        "O":24,
        "P":25,
        "Q":26,
        "R":27,
        "S":28,
        "T":29,
        "U":30,
        "V":31,
    }
    n = 0
    #conversion vers décimal
    for i in range(len(num1)):
        n+=(dicto.get(num1[-i-1])*(b1**i))
    
    res = ""
    #conversion vers base 2
    while n >0:
        res= str(dicto.get(str(n%b2))) + res
        n= n//b2
    return res

#Additionneur bits quelconque
def addany(num1:str,num2:str)->str:
    #On ralonge les variables pour qu'elles soient de même taille
    if len(num1) >= len(num2):
        while len(num2) != len(num1):
            num2 = "0"+num2
    else:
        while len(num1) != len(num2):
            num1 = "0"+num1 
    lenmax = len(num1)
    retenue = 0
    res =""
    for i in range(lenmax):
        #Si l'addition de n1, n2 et la retenue == 1 ou 3 alors la réponse est 1 
        res = "1"+res if int(num1[-i-1])+int(num2[-i-1])+int(retenue) ==(1 or 3) else "0"+res
        #Si l'addition des 3 est supérieur à 1 alors il y a une retenue 
        retenue = 1 if int(num1[-i-1])+int(num2[-i-1])+int(retenue) > 1 else 0
    return res

#Additionneur à nombre de bits fixe 
def addfix(num1:str,num2:str,lenmax:int)->str:
    #On ralonge les variables pour qu'elles soient de même taille
    while len(num1) < lenmax:
        num1 = "0"+num1
    while len(num2) < lenmax:
        num2 = "0"+num2
    retenue = 0
    res =""
    for i in range(lenmax):
            #Si l'addition de n1, n2 et la retenue == 1 ou 3 alors la réponse est 1 
        res = "1"+res if int(num1[-i-1])+int(num2[-i-1])+int(retenue) ==(1 or 3) else "0"+res
        #Si l'addition des 3 est supérieur à 1 alors il y a une retenue 
        retenue = 1 if int(num1[-i-1])+int(num2[-i-1])+int(retenue) > 1 else 0
    return res

#Soustracteur à nombre de bit quelconque
def subany(num1:str,num2:str)->str:
    #on rallonge les nombres pour qui soient de même longueur
    while len(num1) != len(num2):
        if len(num1)>len(num2):
            num2="0"+num2
        else:
            num1="0"+num1
    res =""
    retenue = 0
    for i in range(len(num1)):
        #si la soustraction de n1 avec (n2 et retenue) = 1 ou -1 alors on garde 1
        if int(num1[-i-1])-(int(num2[-i-1])+retenue) in [1,-1]:
            res ="1"+res
        elif int(num1[-i-1])-(int(num2[-i-1])+retenue) in [0,-2]:
            res = "0"+res
        #Si le nombre est négatif alors il y a une retenue
        if int(num1[-i-1])-(int(num2[-i-1])+retenue) < 0:
            retenue=1
        else:
            retenue = 0
    return res

#soustracteur à nombre de bits fixe
def subfix(num1,num2,lenmax):
    #on rallonge les nombres pour qui soient de même longueur
    while len(num1) != lenmax:
        if len(num1)< lenmax:
            num1="0"+num1
        else:
            num1=num1[1:]
    while len(num2) != lenmax:
        if len(num2)< lenmax:
            num2="0"+num2
        else:
            num2=num2[1:]
    res =""
    retenue = 0
    for i in range(lenmax):
        #si la soustraction de n1 avec (n2 et retenue) = 1 ou -1 alors on garde 1
        if int(num1[-i-1])-(int(num2[-i-1])+retenue) in [1,-1]:
            res ="1"+res
        elif int(num1[-i-1])-(int(num2[-i-1])+retenue) in [0,-2]:
            res = "0"+res
        #Si le nombre est négatif alors il y a une retenue
        if int(num1[-i-1])-(int(num2[-i-1])+retenue) < 0:
            retenue=1
        else:
            retenue = 0
    return res

#multiplicateur à nombre de bit quelconque
def multipleany(num1,num2):
    presumlist = []
    crntres =""
    #On multiplie 
    for i in range(len(num1)):
        for j in range(len(num2)):
            crntres = "1"+crntres if (int(num1[-i-1]) and int(num2[-j-1])) == 1 else "0"+crntres
        presumlist.append(crntres)
        crntres = "0"*(i+1)
        #On récupère une liste de binaires à additionner
    #On additionne tout
    while len(presumlist) !=1:
        presumlist.append(addany(presumlist[0],presumlist[1]))
        presumlist.pop(0)
        presumlist.pop(0)
    res = presumlist[0].lstrip("0")
    return res

#multiplicateur à nombre de bit fixe
def multiplefix(num1,num2,lenmax):
    #on mets tout à la longueur demandé
    while len(num1) < lenmax:
        num1 ="0"+num1
    while len(num2) < lenmax:
        num2 ="0"+num2
    presumlist = []
    crntres =""
    #On multiplie
    for i in range(len(num1)):
        for j in range(len(num2)):
            crntres = "1"+crntres if (int(num1[-i-1]) and int(num2[-j-1])) == 1 else "0"+crntres
        presumlist.append(crntres)
        crntres = "0"*(i+1)
    #On additionne
    while len(presumlist) !=1:
        presumlist.append(addany(presumlist[0],presumlist[1]))
        presumlist.pop(0)
        presumlist.pop(0)
    res = presumlist[0]
    #On raccourci pour la bonne longueur
    if len(res) > lenmax:
        while len(res) != lenmax:
            res = res[1:]
    elif len(res) < lenmax:
        while len(res) != lenmax:
            res = "0"+res
    return res

#convertisseur décimal complément à 2 avec choix du nombre de bit
def deccomp2fix(num1,precision):
    n = dectobin(num1)
    while len(n) != precision:
        if len(n) < precision:
            n="0"+n
        elif len(n) > precision:
            n = n[1:] 
    res =""
    for i in n:
        res += "1" if i == "0" else "0"
    num2=""
    while "1" in addfix(n,res,len(n)):
        res =addfix(res,"1",len(res))
    return res

#convertisseur décimal complément à 2 sans choix du nombre de bits
def deccomp2any(num1):
    n = dectobin(num1)
    res =""
    for i in n:
        res += "1" if i == "0" else "0"
    while "1" in addfix(n,res,len(n)):
        res =addfix(res,"1",len(res))
    return res

#convertisseur complément à 2  -> décimal avec choix du nombre de bit
def comp2decfix(num1,lenmax):
    while len(num1) != lenmax:
        if len(num1)> lenmax:
            num1 =num1[:1]
        else:
            num1 ="0"+num1
    res =""
    for i in num1:
        res += "1" if i == "0" else "0"
    res =addfix(res,"1",len(res))
    return bintodec(res)

#convertisseur complément à 2  -> décimal sans choix du nombre de bits
def comp2decany(num1):
    res =""
    for i in num1:
        res += "1" if i == "0" else "0"
    res =addfix(res,"1",len(res))
    return bintodec(res)

#convertisseur décimal flottant
def dectofloatany(n:float)->str:
    try:
        n = float(n)
    except TypeError:
        raise(TypeError("Num isn't float"))
    entiern = dectobin(int(n))
    decimal = str(n)
    try:
        while decimal[0] != ".":
            decimal = decimal[1:]
    except IndexError:
        raise(TypeError("input isn't float, dectofloatany takes one argument n type float, n is "+str(n)))
    decimal = int(decimal[1:])
    decalage = len(str(decimal))
    res = entiern+","
    while decimal != 0 and len(res) < 64:
        decimal *=2
        if decimal >= 1*10**decalage:
            res += "1"
            decimal -= 1*10**decalage
        else:
            res +="0"
    return res
  
#convertisseur decimal flottant sans choix
def dectofloatfix(n:float,precision:int)->str:
    try:
        n = float(n)
    except TypeError:
        "Num isn't float"
    entiern = dectobin(int(n))
    decimal = str(n)
    while decimal[0] != ".":
        decimal = decimal[1:]
    decimal = int(decimal[1:])
    decalage = len(str(decimal))
    res = entiern+","

    while decimal != 0 and len(res) < precision:
        decimal *=2
        if decimal >= 1*10**decalage:
            res += "1"
            decimal -= 1*10**decalage
        else:
            res +="0"

    return res

#convertisseur flottant decimal sans choix
def floattodecany(n:str):
    try:
        if "," not in n:
            raise(TypeError)
    except:
        return ("number isn't a float")
    entier = ""
    while n[0] != ",":
        entier += n[0]
        n = n[1:]
    n = n[1:]
    virgulein = n
    entier = bintodec(entier)
    virguleout = 0
    for i in range(len(virgulein)):
        virguleout += int(virgulein[i])*2**(-i-1)
    return (entier+virguleout)

#convertisseur flottant vers décimal avec choix
def floattodecfix(n:str,precision):
    try:
        if "," not in n:
            raise(TypeError)
    except:
        return ("number isn't a float")
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

#Convertisseur décimal ieee754 précision au choix et sans choix
def dectoieee754(n:int,precision="double"):
    try:
        if precision.lower() != "double" and precision.lower() != "simple":
            raise ValueError("precision isn't Double or Simple")
        decal = 1023 if precision.lower() == "double" else 127
        mantisselen = 52 if precision.lower() == "double" else 23
        exposantlen = 11 if precision.lower() == "double" else 8
        fullresult = ""
        #Le signe
        if n < 0:
            fullresult = "1 "
        else:
            fullresult = "0 "

        n = abs(n)
        fulln = int(n)
        result = ""
        
        #Le nombre 
        while fulln!=0:
            result = str(fulln%(2)) + result
            fulln = fulln//2
        if len(result) > mantisselen+1:
            raise(OverflowError)
        #L'exposant
        exposant =  (dectobin(decal+len(result)-1))
        exposant = "0"*(exposantlen-len(exposant)) +exposant
        result = result[1:]
        #La virgule
        floatn = n - int(n)
        if type(n) == float:
            while floatn!=0 or len(result)<mantisselen:
                floatn*=2
                result+=str(int(floatn))
                floatn -= int(floatn)
        
        #Le tout
        result += "0"*(mantisselen-len(result))
        fullresult += (exposant+" "+result)
        return fullresult
    except OverflowError:
        raise Exception("Num too big")

def comparebin(n1:str,n2:str):
    n1 = n1.lstrip("0")
    n2 = n2.lstrip("0")
    if len(n1) > len(n2):
        return 1
    elif len(n2) > len(n1):
        return 2
    for i in range(len(n1)):
        if n1[i] != n2[i]:
            if n1[i] == "1":
                return 1
            elif n2[i] == "1":
                return 2
    return 3


def addieee754doublepre(n1:str,n2:str):
    #On vérifie que les nombres soient de la même précision
    try:
        if len(n1) != len(n2):
            raise(TypeError)
    except TypeError:
        return TypeError("numbers aren't the same precision : should be double")
    while " " in n1 or " " in n2:
        n1 = n1.replace(" ","")
        n2 = n2.replace(" ","")
    #On récupère l'exponant des nombres
    expon1 = n1[1:12]
    expon2 = n2[1:12]
    #On récupère la mantisse des nombres
    mantissa1 = n1[12:]
    mantissa2 = n2[12:]
    flag = 0
    if comparebin(expon1,expon2) == 1:
        while comparebin(expon1,expon2) == 1:
            expon2 = addfix(expon2,"1",len(expon2))
            if flag == 0:
                mantissa2 = "1"+mantissa2[0:-1]
                flag +=1
            else: 
                mantissa2 = "0"+mantissa2[0:-1]
            exponantfinal = expon1
            
    elif comparebin(expon1,expon2) == 2:
        while comparebin(expon1,expon2) == 2:
            expon1 = addfix(expon1,"1",len(expon1))
            if flag == 0:
                mantissa1 = "1"+mantissa1[0:-1]
            else:
                mantissa1 = "0"+mantissa1[0:-1]
            exponantfinal = expon1
    elif comparebin(expon1,expon2) == 3:
        exponantfinal = expon1
    if n1[0] == n2[0]:
        mantissefinale = addany(mantissa1,mantissa2)
        while len(mantissefinale) > 52:
            exponantfinal = addfix(exponantfinal,"1",11)
            mantissefinale = mantissefinale[1:]
        signefinal = n1[0]
    elif n1[0] != n2[0]:
        if n1[0] == "0":
            mantissefinale = subany(mantissa2,mantissa1)
            while len(mantissefinale) > 52:
                exponantfinal = addfix(exponantfinal,"1",12)
                mantissefinale = mantissefinale[1:]
            signefinal = n1[0]
        elif n2[0] =="1":
            mantissefinale = subany(mantissa1,mantissa2)
            while len(mantissefinale) > 52:
                exponantfinal = addfix(exponantfinal,"1",12)
                mantissefinale = mantissefinale[1:]
            if comparebin(mantissa1,mantissa2) ==2:
                signefinal = "1"
            else:
                signefinal = "0"
        elif n1[0] == "1":
            mantissefinale = subany(mantissa2,mantissa1)
            while len(mantissefinale) > 52:
                exponantfinal = addfix(exponantfinal,"1",12)
                mantissefinale = mantissefinale[1:]
            if comparebin(mantissa1,mantissa2) ==1:
                signefinal = "1"
            else:
                signefinal = "0"
    return (signefinal+" "+exponantfinal+" "+mantissefinale)


def allany(n:int,add:str,sub:str,multiply:str):
    return floattodecany(dectofloatany(comp2decany(deccomp2any(bintodec(multipleany(subany(addany((hextobin(bintohex(dectobin(n)))),add),sub),multiply))))))


