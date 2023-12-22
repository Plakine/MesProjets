data = open("data/jour10.txt").read().splitlines()


def findS():
    for line in range(len(data)):
        for char in range(len(data[line])):
            if data[line][char] == "S":
                return (line, char)
    return -1


def findnextdir(currenty, currentx, lastmove, grid, start=False):
    if start:
        if currentx < len(grid[currenty])-1:
            if grid[currenty][currentx+1] in "J":
                return [(0, -1), (-1, 0)]
            if grid[currenty][currentx+1] in "-":
                return [(0, 1), (0, -1)]
            if grid[currenty][currentx+1] in "7":
                return [(1, 0), (0, -1)]
        if currenty > 0:
            if grid[currenty-1][currentx] == "|":
                return [(-1, 0), (1, 0)]
        if currentx > 0:
            if grid[currenty][currentx-1] in "L":
                return [(0, 1), (-1, 0)]
            if grid[currenty][currentx-1] in "F":
                return [(1,0), (0,1)]
        if currenty < len(grid)-1:
            if grid[currenty+1][currentx] == "|":
                return [(-1, 0), (1, 0)]
    elif grid[currenty][currentx] == "|":
        if lastmove == (1, 0):
            return (1, 0)
        else:
            return (-1, 0)
    elif grid[currenty][currentx] == "-":
        if lastmove == (0, 1):
            return (0, 1)
        else:
            return (0, -1)
    elif grid[currenty][currentx] == "L":
        if lastmove == (1, 0):
            return (0, 1)
        else:
            return (-1, 0)
    elif grid[currenty][currentx] == "J":
        if lastmove == (1, 0):
            return (0, -1)
        else:
            return (-1, 0)
    elif grid[currenty][currentx] == "7":
        if lastmove == (0, 1):
            return (1, 0)
        else:
            return (0, -1)
    elif grid[currenty][currentx] == "F":
        if lastmove == (0, -1):
            return (1, 0)
        else:
            return (0, 1)
    elif grid[currenty][currentx] == 'S' and not start:
        return ("end", "end")
    raise ValueError("None was entered", currenty, currentx, lastmove)


def partie1():
    count = 0
    starty, startx = findS()
    nxdir = findnextdir(starty, startx, (0, 0), data, True)[0]
    while nxdir != ("end", "end"):
        starty = starty + nxdir[0]
        startx = startx + nxdir[1]
        count += 1
        nxdir = findnextdir(starty, startx, nxdir, data)
    return count//2


def extend(old_grid, x, y, nletter):
    newgrid = [["." for j in range(len(old_grid[i//3])*3)] for i in range(len(old_grid)*3)]
    for i in range(len(old_grid)):
        for j in range(len(old_grid[i])):
            letter = old_grid[i][j]
            if letter == "S":
                letter = nletter
            if letter == "F":
                newgrid[i*3+1][j*3+1] = "F"
                newgrid[i*3+1][j*3+2] = "-"
                newgrid[i*3+2][j*3+1] = "|"
            if letter == "7":
                newgrid[i*3+1][j*3+1] = "7"
                newgrid[i*3+1][j*3] = "-"
                newgrid[i*3+2][j*3+1] = "|"
            if letter == "L":
                newgrid[i*3][j*3+1] = "|"
                newgrid[i*3+1][j*3+1] = "L"
                newgrid[i*3+1][j*3+2] = "-"
            if letter == "J":
                newgrid[i*3][j*3+1] = "|"
                newgrid[i*3+1][j*3+1] = "J"
                newgrid[i*3+1][j*3] = "-"
            if letter == "|":
                newgrid[i*3][j*3+1] = "|"
                newgrid[i*3+1][j*3+1] = "|"
                newgrid[i*3+2][j*3+1] = "|"
            if letter == "-":
                newgrid[i*3+1][j*3] = "-"
                newgrid[i*3+1][j*3+1] = "-"
                newgrid[i*3+1][j*3+2] = "-"
    return newgrid


def floodfill(grid_to_fill):
    nums = 1
    queue = set()
    for y in range(len(grid_to_fill)):
        for x in range(len(grid_to_fill[y])):
            if grid_to_fill[y][x] == 0:
                nums += 1
                queue.add((x, y))
                while len(queue) > 0:
                    x1, y1 = queue.pop()
                    grid_to_fill[y1][x1] = nums
                    if x1 > 0:
                        if grid_to_fill[y1][x1-1] == 0:
                            queue.add((x1-1,y1))
                    if x1 < len(grid_to_fill[y1])-1:
                        if grid_to_fill[y1][x1+1] == 0:
                            queue.add((x1+1, y1))
                    if y1 > 0:
                        if grid_to_fill[y1-1][x1] == 0:
                            queue.add((x1, y1-1)) 
                    if y1 < len(grid_to_fill)-1:
                        if grid_to_fill[y1+1][x1] == 0:
                            queue.add((x1, y1+1))
    return grid_to_fill


def partie2():
    x,y = findS()
    new_grid = extend(data, x, y, "|")
    visit_grid = [[0 for i in range(len(new_grid[j]))] for j in range(len(new_grid))]
    starty, startx = findS()
    starty = starty*3+1
    startx = startx*3+1
    x, y = startx, starty
    nxdir = findnextdir(starty, startx, (0, 0), new_grid, True)[0]
    visit_grid[starty][startx] = 1
    starty = starty + nxdir[0]
    startx = startx + nxdir[1]
    while x != startx or y != starty:
        visit_grid[starty][startx] = 1
        starty = starty + nxdir[0]
        startx = startx + nxdir[1]
        nxdir = findnextdir(starty, startx, nxdir, new_grid)
    g = floodfill(visit_grid)
    count = 0
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == 3:
                for i2 in range(max(0, i-1), min(len(g), i+2)):
                    for j2 in range(max(0, j-1), min(len(g[i2]), j+2)):
                        if g[i2][j2] == 1:
                            g[i][j] = 999
            if g[i][j] not in [1, 2, 999] and i > 1 and j > 1 and i < len(g)-2 and j < len(g[i])-2:
                count += 1
    return count//9


print("Jour 10: \n  Partie 1:", (partie1()), "\n  Partie 2:", (partie2()))
