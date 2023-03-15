x"""
Advent Of Code
jour 8 
Partie 1
Dentiste 10h45 vendredi
"""
Data = open("2022/Data/j8.txt")
Cleaned_Data = [el.strip("\n") for el in Data.readlines()]

def up(line,col):
    startline = line
    startcol = col
    nline = line-1
    i=1
    try:
        if nline == -1:
            return 0
        while Cleaned_Data[startline][startcol] > Cleaned_Data[nline][col]:
            nline -= 1
            if nline == -1:
                return i
            i+=1
        return i
    except IndexError:
        return i

def down(line,col,debug=0):
    startline = line
    startcol = col
    nline = line+1
    i=0
    try:
        if line == len(Cleaned_Data)-1:
            return 0
        if nline == len(Cleaned_Data):
            return 0
        while Cleaned_Data[startline][startcol] > Cleaned_Data[nline][col]:
            nline += 1
            i+=1
        return i
    except IndexError:
        return i

def left(line,col):
    startline = line
    startcol = col
    ncol = col-1
    i=1
    try:
        if ncol == -1:
            return 0
        while Cleaned_Data[startline][startcol] > Cleaned_Data[line][ncol]:
            ncol -= 1
            if ncol == -1:
                return i
            i+=1
        return i
    except IndexError:
        return i

def right(line,col):
    startline = line
    startcol = col
    ncol = col+1
    i=1
    try:
        if ncol == len(Cleaned_Data[line]):
            return 0
        while Cleaned_Data[startline][startcol] > Cleaned_Data[line][ncol]:
            ncol += 1
            i+=1
        return i
        
    except IndexError:
        return i

def main():
    """
    La fonction principale de ce programme,
    """
    score= []
    for line in range(len(Cleaned_Data)):
        for col in range(len(Cleaned_Data[line])):
            score.append(up(line,col) * down(line,col) * left(line,col) * right(line,col))
    return max(score)
print(main())