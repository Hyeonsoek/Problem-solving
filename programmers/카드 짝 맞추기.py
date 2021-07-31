from queue import PriorityQueue as PQ
from itertools import permutations
from collections import defaultdict

import time

dirr = [[0,1],[0,-1],[1,0],[-1,0]]

def make_order(board):
    global number_set
    number_set = defaultdict(list)
    
    for x in range(4):
        for y in range(4):
            if board[x][y] != 0:
                number_set[board[x][y]].append((x,y))
    
    order = [key for key in number_set.keys()]
    return list(permutations(order))

def isinboard(y, x):
    return 0 <= x < 4 and 0 <= y < 4

def move(y, x, mv):
    global newboard
    ny, nx = y, x

    while True:
        _ny = ny + mv[0]
        _nx = nx + mv[1]
        if not isinboard(_ny, _nx): return ny, nx
        if newboard[_ny][_nx] != 0: return _ny, _nx
            
        ny = _ny
        nx = _nx

    return -1, -1

def find_target(target_y, target_x, start_y, start_x):
    
    global newboard
    
    check = [[0,0,0,0] for _ in range(4)]
    pq = PQ()
    
    check[start_y][start_x] = 1
    pq.put((1, start_y, start_x)) # cost, x, y
    
    while not pq.empty():
        cost, y, x = pq.get()

        if x == target_x and y == target_y:
            return cost
        
        for ydir, xdir in dirr:
            xx = x + xdir
            yy = y + ydir

            if isinboard(yy, xx):
                if not check[yy][xx]:
                    check[yy][xx] = 1
                    pq.put((cost+1, yy, xx))


            yy, xx = move(y, x, [ydir, xdir])

            if not check[yy][xx]:
                check[yy][xx] = 1
                pq.put((cost+1, yy, xx))

    return -1

def backtrack(start_y, start_x, order, idx, cost):
    global number_set, newboard

    if idx == len(order):
        return cost

    loc1, loc2 = number_set[order[idx]]
    yy1, xx1 = loc1
    yy2, xx2 = loc2

    ret1 = find_target(yy1, xx1, start_y, start_x)
    ret1 += find_target(yy2, xx2, yy1, xx1)
    newboard[yy1][xx1] = 0
    newboard[yy2][xx2] = 0

    ret1 = backtrack(yy2, xx2, order, idx + 1, cost + ret1)

    newboard[yy1][xx1] = order[idx]
    newboard[yy2][xx2] = order[idx]

    ret2 = find_target(yy2, xx2, start_y, start_x)
    ret2 += find_target(yy1, xx1, yy2, xx2)

    newboard[yy1][xx1] = 0
    newboard[yy2][xx2] = 0

    ret2 = backtrack(yy1, xx1, order, idx + 1, cost + ret2)

    newboard[yy1][xx1] = order[idx]
    newboard[yy2][xx2] = order[idx]

    ret = min(ret1, ret2)

    return ret


def solution(board, r, c):
    answer = 987654321
    order = make_order(board)

    global newboard
    newboard = board[:] 

    for o in order:
        result = backtrack(r, c, o, 0, 0)
        if result < answer:
            answer = result

    return answer


start = time.time()

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))
print(time.time() - start)

start = time.time()
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],0,1))
print(time.time() - start)

start = time.time()
print(solution([[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]], 0, 0))
print(time.time() - start)