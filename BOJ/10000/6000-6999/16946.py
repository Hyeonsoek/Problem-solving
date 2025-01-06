import sys
from collections import deque
direc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]
    
    index = 0
    count = [[(-1, -1)] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if board[x][y] == '0' and count[x][y] == (-1, -1):
                visited = set([(x, y)])
                queue = deque([(x, y)])
                while queue:
                    nx, ny = queue.popleft()
                    
                    for xd, yd in direc:
                        xx = xd + nx
                        yy = yd + ny
                        if 0 <= xx < n and 0 <= yy < m\
                                and (xx, yy) not in visited\
                                and board[xx][yy] == '0':
                            visited.add((xx, yy))
                            queue.append((xx, yy))
                
                for xx, yy in visited:
                    count[xx][yy] = (index, len(visited))
                index += 1
    
    result = [[0] * m for _ in range(n)]
    
    for x in range(n):
        for y in range(m):
            if board[x][y] == '1':
                cluster = set()
                result[x][y] = 1
                for xd, yd in direc:
                    xx = x + xd
                    yy = y + yd
                    if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == '0':
                        ii, cc = count[xx][yy]
                        if ii not in cluster:
                            result[x][y] += cc
                            cluster.add(ii)
    
    for x in range(n):
        print(''.join(map(lambda xx: str(xx % 10), result[x])))

solve()