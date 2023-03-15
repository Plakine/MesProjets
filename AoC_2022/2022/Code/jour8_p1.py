"""
Advent Of Code
jour 8 
Partie 1
Dentiste 10h45 vendredi
"""
Data = open("2022/Data/j8.txt")
Treated_data = [el.strip("\n") for el in Data.readlines()]

def up(line,col):
    startline = line
    startcol = col
    nline = line-1
    try:
        if nline == -1:
            return True
        while Treated_data[startline][startcol] > Treated_data[nline][col]:
            nline -= 1
            if nline == -1:
                return True
        return False
    except IndexError:
        return True

def down(line,col):
    startline = line
    startcol = col
    nline = line+1
    try:
        while Treated_data[startline][startcol] > Treated_data[nline][col]:
            nline += 1
        return False
    except IndexError:
        return True

def left(line,col):
    startline = line
    startcol = col
    ncol = col-1
    try:
        if ncol == -1:
            return True
        while Treated_data[startline][startcol] > Treated_data[line][ncol]:
            ncol -= 1
            if ncol == -1:
                return True
        return False
    except IndexError:
        return True

def right(line,col):
    startline = line
    startcol = col
    ncol = col+1
    try:
        while Treated_data[startline][startcol] > Treated_data[line][ncol]:
            ncol += 1
        return False
    except IndexError:
        return True

def main():
    """
    La fonction principale de ce programme,
    """
    score= 0
    for line in range(len(Treated_data)):
        for col in range(len(Treated_data[line])):
            if up(line,col) or down(line,col) or left(line,col) or right(line,col):
                score+=1
    return score
print(main())