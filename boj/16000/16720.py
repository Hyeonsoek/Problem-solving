import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    board = [list(map(int, input().strip())) for _ in range(n-2)]
    
    result = n * 4
    for x in range(4):
        dist = n + 2
        for xx in range(n - 2):
            front = 0
            while board[xx][(x + front) % 4] == 1:
                front += 1

            back = 0
            while board[xx][(x - back) % 4] == 1:
                back += 1
            
            dist += min(front, back)

        result = min(result, dist)
    
    print(result)

solve()