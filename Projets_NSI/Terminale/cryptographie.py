from math import gcd, log2
from random import randint


class message:
    def __init__(self, message, p, q):
        self.message = message
        self.cle_prive, self.cle_publique = rsa(p, q)
        print("log : key generated successfully")

    def encode(self):
        vmax = int(log2(self.cle_publique[1]))
        # On convertit le message en binaire
        res = ""
        rlist = []
        for i in self.message:
            e = ord(i)
            res += bin(e).lstrip("0b")
        # on découpe le message
        while len(res) % vmax != 0:
            res = "0"+res
        for i in range(len(res)//vmax):
            rlist.append(res[i*vmax:(i+1)*vmax])
        res = ""
        for i in range(len(rlist)):
            mc = int(rlist[i], 2)**self.cle_publique[0] % self.cle_publique[1]
            rlist[i] = bin(mc).lstrip("0b").zfill(7)
            res += rlist[i]
        r2 = ""
        while len(res)%7 != 0:
            res = "0" + res
        for i in range(len(res)//7):
            print(res[i*7: (i+1)*7], "e")
            r2 += chr(int(res[i*7: (i+1)*7], 2))
        self.message = r2
        return r2

    def decode(self):
        res = []
        vmax = int(log2(self.cle_publique[1]))
        for i in self.message:
            res.append(bin(ord(i)).lstrip("0b").zfill(7))
        for i in range(len(res)):
            res[i] = int(res[i], 2)**self.cle_prive[0] % self.cle_prive[1]
            res[i] = bin(res[i]).lstrip("0b").zfill(vmax)
        r2 = ""
        for i in res:
            r2 += i
        res = r2
        while len(res) % 7 != 0:
            res = res[1:]
        msg = ""
        for i in range(len(res)//7):
            print(int(res[i*7:(i+1)*7], 2))
            msg += chr(int(res[i*7:(i+1)*7], 2))
        return msg


def phi(p, q):
    return (p-1)*(q-1)


def getpremier(phin):
    e = 3
    res = []
    while e < phin:
        if gcd(e, phin) == 1:
            res.append(e)
        e += 1
    return res[randint(0, len(res)-1)]


def eu_etend(r, r1, u=1, v=0, u1=0, v1=1):
    if r1 > 0:
        q = r//r1
        return eu_etend(r1, (r-q*r1), u1, v1, (u-u1*q), (v-v1*q))
    else:
        return (u, v)


def rsa(p, q):
    n = p*q
    phn = phi(p, q)
    d = -1
    while d < 0:
        e = getpremier(phn)
        clpub = (e, n)
        if e > phn:
            d = eu_etend(e, phn)[0]
        else:
            d = eu_etend(phn, e)[1]
    clpriv = (d, n)
    return clpriv, clpub


m = message("e", 593, 457)
m.encode()
print(m.decode())
