from typing import List


def situation_finale(n: int, m: int, villes: List[str], actions: List[str]) -> None:
    """
    :param n: le nombre de villes autour de Midgard
    :param m: le nombre d'années avant le Ragnarök
    :param villes: le nom des villes autour de Midgard, en partant de la queue de Jörmungandr

    :param actions: la liste des actions prochaines de Jörmungandr
    """
    # TODO Afficher, sur une ligne par ville, la liste des villes qui seront
    # rencontrées lors du Ragnarök, dans l'ordre, en partant de la queue de
    # Jörmungandr jusqu'à sa tête.
    pos = 0
    mov = 1
    eaten = []
    print(villes[pos:]+villes[:pos])
    for i in range(m):
        if actions[i] == "A":
            pos = (pos+mov)%n
        elif actions[i] == "M":
            n -= 1
            eaten.append(villes[pos])
            villes.pop(pos)
        elif actions[i] == "R":
            if mov == 1:
                mov = -1
            else:
                mov = 1
            pos = (pos+mov)%n
        elif actions[i] == "C":
            villes.insert(pos, eaten[-1])
            eaten.pop()
        print(villes[pos:]+villes[:pos])
    if mov == 1:
        return villes[pos:]+villes[:pos]
    else:
        return villes[pos:]+villes[:pos][::-1]
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    villes = [input() for _ in range(n)]
    actions = list(input())
    result = situation_finale(n, m, villes, actions)
    for i in result:
        print(i)