import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    board = [[*map(int, input().split())] for _ in range(n)]

    sx = sy = 0
    for x in range(n):
        for y in range(n):
            if not board[x][y]:
                sx, sy = x, y

    row = [  ]
    column = [ ]
    
    for x in range(n):
        sumx = sumy = 0
        countx = county = 0
        for y in range(n):
            sumx += board[x][y]
            countx += board[x][y] != 0
            sumy += board[y][x]
            county += board[y][x] != 0
        row.append((sumx, countx))
        column.append((sumy, county))
    
    if len(set(row)) > 2 or len(set(column)) > 2:
        return -1

    row = [ x[0] for x in row ]
    column = [ x[0] for x in column ]

    rowvalue = -1
    for x in set(row):
        if x != row[sx]:
            rowvalue = x - row[sx]
            break
    
    if rowvalue < 0:
        return -1
        
    columnvalue = -1
    for x in set(column):
        if x != column[sy]:
            columnvalue = x - column[sy]
            break
    
    if columnvalue < 0:
        return -1
    
    if rowvalue != columnvalue:
        return -1
    
    lr, rl = 0, 0
    for x in range(n):
        lr += board[x][x] if board[x][x] else rowvalue
        rl += board[x][n-x-1] if board[x][n-x-1] else rowvalue
    
    return rowvalue if lr == rl else -1
    
print(solve())