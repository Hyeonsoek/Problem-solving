import sys
input = sys.stdin.readline
UDRL = {'U': [1, 0], 'D':[-1, 0], 'R':[0, 1], 'L':[0, -1]}

def solve():
    n, k = map(int, input().split())
    
    visited = {}
    for _ in range(n):
        xx, yy = map(int, input().split())
        visited[xx,yy] = True
    
    sx = sy = 0
    query = input().strip()
    for i in range(k):
        dy, dx = UDRL[query[i]]
        nx = sx + dx
        ny = sy + dy
        if (nx, ny) not in visited:
            sx = nx
            sy = ny
    print(sx, sy)

solve()