import hashlib

# Partie 1
def partie1(clé):
    i = 1
    while True:
        hash = hashlib.md5((clé+str(i)).encode()).hexdigest()
        if hash[:5] == "00000":
            return i
        i += 1
    return False

print(f"Partie : {partie1('bgvyzdsv')}")


def partie2(clé):
    i = 1
    while True:
        hash = hashlib.md5((clé+str(i)).encode()).hexdigest()
        if hash[:6] == "000000":
            return i
        i += 1
    return False

print(f"Partie : {partie2('bgvyzdsv')}")