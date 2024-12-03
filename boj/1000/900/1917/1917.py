from copy import deepcopy

n = 6
pivot = [
    ['1000', '1111', '1000'],
    ['0100', '1111', '1000'],
    ['0010', '1111', '1000'],
    ['0001', '1111', '1000'],
    ['0100', '1111', '0100'],
    ['0010', '1111', '0100'],
    ['00111', '11100'],
    ['0011', '0110', '1100'],
    ['0011', '1110', '1000'],
    ['1100', '0111', '0100'],
    ['0100', '1110', '0011']
]
p = len(pivot)

for i in range(p):
    pivot.append(deepcopy(pivot[i])[::-1])

p += p

for i in range(p):
    for x in range(len(pivot[i])):
        pivot[i][x] = [*map(int, pivot[i][x])]

def rotate(index, count):
    copy = deepcopy(pivot[index])
    match count:
        case 1:
            copy = list(zip(*copy))[::-1]
        case 2:
            copy = list(map(lambda x: x[::-1], copy))
        case 3:
            copy = list(zip(*copy))
    return copy

def innershape(board, i, j, k, r):
    shape = rotate(k, r)
    X = len(shape)
    Y = len(shape[0])
    for xx in range(i, i + X):
        for yy in range(j, j + Y):
            if not (0 <= xx < n and 0 <= yy < n):
                return False
            if board[xx][yy] != shape[xx - i][yy - j]:
                return False
    
    return True

def isinnershape(board, i, j):
    for k in range(p):
        for r in range(4):
            if innershape(board, i, j, k, r):
                return True
    
    return False

def solve():
    board = [[*map(int, input().split())] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if isinnershape(board, i, j):
                return 'yes'
    
    return 'no'

for _ in range(3):
    print(solve())