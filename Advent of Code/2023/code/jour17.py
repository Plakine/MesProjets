# Algorithme de Dijkstra
import heapq as pq
data = open("data/jour17.txt").read().splitlines()
for i in range(len(data)):
    data[i] = [int(j) for j in data[i]]

def partie1():
    visited_nodes = {}
    priority_queue = []
    x, y = 0, 0
    y_end = len(data)-1
    x_end = len(data[y_end])-1
    count = 0
    lastmove = ""
    cost = 0
    while x != x_end or y_end != y:
        if y > 0 and (lastmove != "up" or count < 2) and lastmove != "down":
            if lastmove != "up":
                tempcount = 0
            else:
                tempcount = count+1
            tempcost = cost + data[y-1][x]
            if (x, y-1, lastmove, tempcount) in visited_nodes.keys():
                if visited_nodes[(x, y-1, lastmove, tempcount)] > tempcost:
                    visited_nodes[(x, y-1, lastmove, tempcount)] = tempcost
                    pq.heappush(priority_queue, (tempcost, x, y-1, "up", tempcount))
            else:
                visited_nodes[(x, y-1, lastmove, tempcount)] = tempcost
                pq.heappush(priority_queue, (tempcost, x, y-1, "up", tempcount))
        if y < len(data)-1 and (lastmove != "down" or count < 2) and lastmove != "up":
            if lastmove != "down":
                tempcount = 0
            else:
                tempcount = count+1
            tempcost = cost + data[y+1][x]
            if (x, y+1, lastmove, tempcount) in visited_nodes.keys():
                if visited_nodes[(x, y+1, lastmove, tempcount)] > tempcost:
                    visited_nodes[(x, y+1, lastmove, tempcount)] = tempcost
                    pq.heappush(priority_queue, (tempcost, x, y+1, "down", tempcount))
            else:
                visited_nodes[(x, y+1, lastmove, tempcount)] = tempcost
                pq.heappush(priority_queue, (tempcost, x, y+1, "down", tempcount))
        if x > 0 and (lastmove != "left" or count < 2) and lastmove != "right":
            if lastmove != "left":
                tempcount = 0
            else:
                tempcount = count+1
            tempcost = cost + data[y][x-1]
            if (x-1, y, lastmove, tempcount) in visited_nodes.keys():
                if visited_nodes[(x-1, y, lastmove, tempcount)] > tempcost:
                    visited_nodes[(x-1, y, lastmove, tempcount)] = tempcost
                    pq.heappush(priority_queue, (tempcost, x-1, y, "left", tempcount))
            else:
                visited_nodes[(x-1, y, lastmove, tempcount)] = tempcost
                pq.heappush(priority_queue, (tempcost, x-1, y, "left", tempcount))
        if x < x_end and (lastmove != "right" or count < 2) and lastmove != "left":
            if lastmove != "right":
                tempcount = 0
            else:
                tempcount = count+1
            tempcost = cost + data[y][x+1]
            if (x+1, y, lastmove, tempcount) in visited_nodes.keys():
                if visited_nodes[(x+1, y, lastmove, tempcount)] > tempcost:
                    visited_nodes[(x+1, y, lastmove, tempcount)] = tempcost
                    pq.heappush(priority_queue, (tempcost, x+1, y, "right", tempcount))
            else:
                visited_nodes[(x+1, y, lastmove, tempcount)] = tempcost
                pq.heappush(priority_queue, (tempcost, x+1, y, "right", tempcount))
        cost, x, y, lastmove, count = pq.heappop(priority_queue)
    return cost
def partie2():
    visited_nodes = {}
    priority_queue = []
    x, y = 0, 0
    y_end = len(data)-1
    x_end = len(data[y_end])-1
    count = 0
    lastmove = ""
    cost = 0
    while x != x_end or y_end != y:
        if ((count == 0 or lastmove != "up") and (y > 3 and (lastmove != "up" or count < 9) and lastmove != "down")) or ((count >= 3 and lastmove == "up") and (y > 0 and (lastmove != "up" or count < 9) and lastmove != "down")):
            if lastmove != "up":
                tempcount = 3
                ny = y-4
            elif count >= 3:
                tempcount = count+1
                ny = y-1
            tempcost = cost 
            for nx2 in range(ny, y):
                tempcost += data[nx2][x]
            if (x, ny, lastmove, tempcount) in visited_nodes.keys():
                if visited_nodes[(x, ny, lastmove, tempcount)] > tempcost:
                    visited_nodes[(x, ny, lastmove, tempcount)] = tempcost
                    pq.heappush(priority_queue, (tempcost, x, ny, "up", tempcount))
            else:
                visited_nodes[(x, ny, lastmove, tempcount)] = tempcost
                pq.heappush(priority_queue, (tempcost, x, ny, "up", tempcount))
        if ((count == 0 or lastmove != "down") and (y+4 < len(data) and (lastmove != "down" or count < 9) and lastmove != "up")) or ((count >= 3 and lastmove == "down")and (y < len(data)-1 and (lastmove != "down" or count < 9) and lastmove != "up")):
            if lastmove != "down":
                tempcount = 3
                ny = y+4
            elif count >= 3:
                tempcount = count+1
                ny = y+1
            tempcost = cost
            for nx2 in range(y+1, ny+1):
                tempcost += data[nx2][x]
            if (x, ny, lastmove, tempcount) in visited_nodes.keys():
                if visited_nodes[(x, ny, lastmove, tempcount)] > tempcost:
                    visited_nodes[(x, ny, lastmove, tempcount)] = tempcost
                    pq.heappush(priority_queue, (tempcost, x, ny, "down", tempcount))
            else:
                visited_nodes[(x, ny, lastmove, tempcount)] = tempcost
                pq.heappush(priority_queue, (tempcost, x, ny, "down", tempcount))
        if ((count == 0 or lastmove != "left") and (x > 3 and (lastmove != "left" or count < 9) and lastmove != "right")) or ((count >= 3 and lastmove == "left") and (x > 3 and (lastmove != "left" or count < 9) and lastmove != "right")):
            if lastmove != "left":
                tempcount = 3
                nx = x-4
            elif count >= 3:
                tempcount = count+1
                nx = x-1
            tempcost = cost 
            for nx2 in range(nx, x):
                tempcost += data[y][nx2]
            if (nx, y, lastmove, tempcount) in visited_nodes.keys():
                if visited_nodes[(nx, y, lastmove, tempcount)] > tempcost:
                    visited_nodes[(nx, y, lastmove, tempcount)] = tempcost
                    pq.heappush(priority_queue, (tempcost, nx, y, "left", tempcount))
            else:
                visited_nodes[(nx, y, lastmove, tempcount)] = tempcost
                pq.heappush(priority_queue, (tempcost, nx, y, "left", tempcount))
        if ((count == 0 or lastmove != "right") and (x+3 < x_end and (lastmove != "right" or count < 9) and lastmove != "left")) or ((count >= 3 and lastmove == "right") and (x < x_end and (lastmove != "right" or count < 9) and lastmove != "left")):
            if lastmove != "right":
                tempcount = 3
                nx = x+4
            elif count >= 3:
                tempcount = count+1
                nx = x+1
            tempcost = cost 
            for nx2 in range(x+1, nx+1):
                tempcost += data[y][nx2]
            if (nx, y, lastmove, tempcount) in visited_nodes.keys():
                if visited_nodes[(nx, y, lastmove, tempcount)] > tempcost:
                    visited_nodes[(nx, y, lastmove, tempcount)] = tempcost
                    pq.heappush(priority_queue, (tempcost, nx, y, "right", tempcount))
            else:
                visited_nodes[(nx, y, lastmove, tempcount)] = tempcost
                pq.heappush(priority_queue, (tempcost, nx, y, "right", tempcount))
        cost, x, y, lastmove, count = pq.heappop(priority_queue)
    return cost


print("Jour 17: \n  Partie 1:", (partie1()), "\n  Partie 2:", (partie2()))
