import sys
input = sys.stdin.readline

MAX = 1001

def solve():
    board = [[0] * MAX for _ in range(MAX)]
    count = [0] * MAX

    n = int(input())
    for k in range(1, n + 1):
        sx, sy, width, height = map(int, input().split())
        x, y = sx, sy
        while y < sy + height:
            count[board[x][y]] -= 1
            board[x][y] = k
            
            x += 1
            if x == sx + width:
                x = sx
                y += 1
        
        count[k] += width * height

    for k in range(1, n + 1):
        print(count[k])
        
solve()