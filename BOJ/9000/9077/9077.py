import sys
input = sys.stdin.readline

MAX = 10000

def solve():
    n = int(input())
    board = [[0] * (MAX + 1) for _ in range(MAX + 1)]
    
    result = 0
    for x in range(n):
        xx, yy = map(int, input().split())
        for sx in range(xx, xx + 11):
            for sy in range(yy, yy + 11):
                if sx <= MAX and sy <= MAX:
                    board[sx][sy] += 1
                    result = max(result, board[sx][sy])

    print(result)

for _ in range(int(input())):
    solve()