import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    row = [*map(int, input().split())]
    column = [*map(int, input().split())]
    board = [[0] * n for _ in range(n)]
    
    if sum(row) != sum(column):
        print(-1)
        return
    
    column = [[column[x], x] for x in range(n)]
    for x in range(n):
        index = 0
        column.sort(reverse=True)
        while index < n and row[x]:
            if column[index][0]:
                row[x] -= 1
                column[index][0] -= 1
                board[x][column[index][1]] = 1
            
            index += 1
        
        if row[x]:
            print(-1)
            return
    
    print(1)
    for x in board:
        print(*x, sep='')

solve()