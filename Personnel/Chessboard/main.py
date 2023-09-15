"""
Jeu d'échec
V1
création 2 Juillet 2023
"""

class chess:

    class Player:
        def __init__(self, couleur) -> None:
            self.couleur = couleur
            self.can_castle = True
            self.is_checked = False
    def __init__(self) -> None:
        self.Blanc = self.Player("blanc")
        self.Noir = self.Player("noir")
        # crée l'échiquier
        self.board = [["c", "n", "b", "q", "k", "b", "n", "c"],
                      ["p", "p", "p", "p", "p", "p", "p", "p"],
                      [".", ".", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", ".", "."],
                      [".", ".", "b", ".", ".", ".", ".", "."],
                      ["P", "P", "P", "P", "P", "P", "P", "P"],
                      ["C", "N", "B", "K", "Q", "B", "N", "C"]]
        self.toplay = "Blanc"
    
    def turn(self):
        validmoves = {}
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                ele = self.board[i][j]
                if ele == "P":
                    if i == 6:
                        validmoves[str(i)+","+str(j)] = [(i-1, j), (i-2, j)]
                    else:
                        validmoves[str(i)+","+str(j)] = [(i-1, j)]
                    if j > 0:
                        if self.board[i-1][j-1] != "." and self.board[i-1][j-1].islower():
                            validmoves[str(i)+","+str(j)].append((i-1, j-1))
                    if j < 7:
                        if self.board[i-1][j+1] != "." and self.board[i-1][j+1].islower():
                            validmoves[str(i)+","+str(j)].append((i-1, j+1))
                if ele == "p":
                    if i == 1:
                        validmoves[str(i)+","+str(j)] = [(i+1, j), (i-2, j)]
                    else:
                        validmoves[str(i)+","+str(j)] = [(i+1, j)]
                    if j > 0:
                        if self.board[i+1][j-1] != "." and self.board[i+1][j-1].islower():
                            validmoves[str(i)+","+str(j)].append((i+1, j-1))
                    if j < 7:
                        if self.board[i+1][j+1] != "." and self.board[i+1][j+1].islower():
                            validmoves[str(i)+","+str(j)].append((i+1, j+1))
        print(validmoves)
        source = input("case de départ (format a0): ")
        destination = input("case de départ (format a0): ")
        dicto = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            'e': 4,
            "f": 5,
            "g": 6,
            "h": 7
        }
        source = [int(dicto[source[0]]), int(source[1])]
        destination = [int(dicto[destination[0]]), int(destination[1])]
        self.move(source, destination)

    def move(self, source, destination):
        temp = self.board[source[0]][source[1]]
        if (temp == temp.isupper() and self.toplay != "Blanc") or (temp.islower() and self.toplay == "Blanc"):
            return -1
        self.board[source[0]][source[1]] = "."
        self.board[destination[0]][destination[1]] = temp

jeu = chess()
jeu.turn()
print(jeu.board)