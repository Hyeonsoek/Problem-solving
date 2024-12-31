import sys
MIN = -sys.maxsize
input = sys.stdin.readline

def solve():
    n = int(input())
    board = [[*map(int, input().split())] for _ in range(2)]
    
    cache = [[MIN] * n for _ in range(2)]
    
    cache[0][n-1] = board[0][n-1] + board[1][n-1]
    cache[1][n-1] = max(board[1][n-1], cache[0][n-1])
    
    for j in reversed(range(n-1)):
        for i in range(2):
            cache[i][j] = max(
                cache[i][j+1] + board[i][j],
                cache[i][j+1] + board[i][j] + board[i^1][j],
                cache[i^1][j+1] + board[i][j] + board[i^1][j]
            )
    
    print(cache[0][0])

solve()