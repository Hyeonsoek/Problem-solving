import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    board = [[*map(int, input().split())] for _ in range(n)]
    cache = [[0] * m for _ in range(n)]
    
    cache[0][0] = board[0][0]
    
    for i in range(1, n):
        cache[i][0] = cache[i-1][0] + board[i][0]
    
    for j in range(1, m):
        cache[0][j] = cache[0][j-1] + board[0][j]
    
    for i in range(1, n):
        for j in range(1, m):
            cache[i][j] = max(cache[i - 1][j], cache[i][j - 1]) + board[i][j]
    
    print(cache[n - 1][m - 1])
    
solve()