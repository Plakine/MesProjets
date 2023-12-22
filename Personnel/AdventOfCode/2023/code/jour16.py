data = open("data/jour16.txt").read().splitlines()

class Beam:
    def __init__(self, posx, posy, dirx, diry):
        self.px = posx
        self.py = posy
        self.dx = dirx
        self.dy = diry
    def move(self):
        self.px += self.dx
        self.py += self.dy
def simulate(startx, starty, dirx, diry):
    Beams = [Beam(startx,starty,dirx,diry)]
    energized_cases = {}
    while len(Beams) > 0:
        for beam in Beams:
            beam.move()
            if beam.py >= len(data) or beam.py < 0 or beam.px >= len(data[beam.py]) or beam.px < 0:
                Beams.remove(beam)
            else:
                case = data[beam.py][beam.px]
                if case == "|" and beam.dx != 0:
                    beam.dy = -1
                    beam.dx = 0
                    Beams.append(Beam(beam.px, beam.py, 0, 1))
                elif case == "-" and beam.dy != 0:
                    beam.dy = 0
                    beam.dx = -1
                    Beams.append(Beam(beam.px, beam.py, 1, 0))
                elif case in "/":
                    temp = beam.dx
                    beam.dx = -beam.dy
                    beam.dy = -temp
                elif case == "\\":
                    temp = beam.dx
                    beam.dx = beam.dy
                    beam.dy = temp
                if (beam.px, beam.py) in energized_cases:
                    if  (beam.dx, beam.dy) in energized_cases[(beam.px, beam.py)] :
                        Beams.remove(beam)
                    else:
                        energized_cases[(beam.px, beam.py)].append((beam.dx, beam.dy))
                if (beam.px, beam.py) not in energized_cases.keys():
                    energized_cases[(beam.px, beam.py)] = [(beam.dx, beam.dy)]
    return len(energized_cases)
def partie1():
    return simulate(-1,0,1,0)
def partie2():
    res = []
    # TOP ROW
    for i in range(len(data[0])):
        res.append(simulate(i-1,0,0,1))
    # Bottom  ROW
    for i in range(len(data[-1])):
        res.append(simulate(i+1,0,0,-1))
    # Left ROW
    for i in range(len(data)):
        res.append(simulate(-1,i,1,0))
    # right ROW
    for i in range(len(data)):
        res.append(simulate(len(data[i])+1,i,-1,0))
    return max(res)


print("Jour 16: \n  Partie 1:", (partie1()), "\n  Partie 2:", (partie2()))
