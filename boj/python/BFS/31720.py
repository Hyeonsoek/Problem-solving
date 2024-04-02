import sys
import collections
dirr = {'U': (-1, 0), 'D': (1, 0), 'R':(0, 1), 'L':(0, -1)}
input = sys.stdin.readline

def solve():
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    O = input().strip()
    R = input().strip()
    len_O = len(O)
    len_R = len(R)

    sx, sy = 0, 0
    ex, ey = 0, 0

    for x in range(n):
        for y in range(n):
            if board[x][y] == 'S':
                sx, sy = x, y
            if board[x][y] == 'E':
                ex, ey = x, y
    
    visited = [[[[0] * n for _ in range(n)]
                    for _ in range(len_O + 1)]
                        for _ in range(len_R + 1)]
    visited[0][0][sx][sy] = 1
    
    queue = collections.deque([(sx, sy, 0, 0)])
    while queue:
        cx, cy, so, sr = queue.popleft()
        
        if cx == ex and cy == ey:
            return so + sr
        
        if so < len_O:
            dx, dy = dirr[O[so]]
            xx, yy = cx + dx, cy + dy
            if 0 <= xx < n and 0 <= yy < n:
                if board[xx][yy] == '#':
                    if not visited[sr][so + 1][cx][cy]:
                        visited[sr][so + 1][cx][cy] = 1
                        queue.append((cx, cy, so + 1, sr))
                else:
                    if not visited[sr][so + 1][xx][yy]:
                        visited[sr][so + 1][xx][yy] = 1
                        queue.append((xx, yy, so + 1, sr))
            else:
                if not visited[sr][so + 1][cx][cy]:
                    visited[sr][so + 1][cx][cy] = 1
                    queue.append((cx, cy, so + 1, sr))
                
        if sr < len_R:
            dx, dy = dirr[R[sr]]
            xx, yy = cx + dx, cy + dy
            if 0 <= xx < n and 0 <= yy < n:
                if board[xx][yy] == '#':
                    if not visited[sr + 1][so][cx][cy]:
                        visited[sr + 1][so][cx][cy] = 1
                        queue.append((cx, cy, so, sr + 1))
                else:
                    if not visited[sr + 1][so][xx][yy]:
                        visited[sr + 1][so][xx][yy] = 1
                        queue.append((xx, yy, so, sr + 1))
            else:
                if not visited[sr + 1][so][cx][cy]:
                    visited[sr + 1][so][cx][cy] = 1
                    queue.append((cx, cy, so, sr + 1))
                    
    return -1
        
    
print(solve())