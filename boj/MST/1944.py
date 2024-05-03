from collections import deque
from sys import stdin
input = stdin.readline
dirr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N, M = map(int, input().split())
miro = [list(input()) for _ in range(N)]

def bfs(sy, sx):
    check = [ [-1 for _ in range(N)] for _ in range(N) ]
    check[sy][sx] = 0
    
    queue = deque()
    queue.append((sy, sx))
    
    while queue:
        y, x = queue.popleft()
        
        for ydir, xdir in dirr:
            yy, xx = ydir + y, xdir + x
            if 0 <= yy < N and 0 <= xx < N and check[yy][xx] == -1 and miro[yy][xx] != '1':
                check[yy][xx] = check[y][x] + 1
                queue.append((yy, xx))

    return check

start = (0, 0)
vertices = []
for y in range(N):
    for x in range(N):
        if miro[y][x] == '0' or miro[y][x] == '1':
            continue
        
        if miro[y][x] == 'S':
            start = (y, x)
            
        vertices.append((y, x))

GRAPH = []

for x in range(M + 1):
    sy, sx = vertices[x]
    cost = bfs(sy, sx)
    
    for y in range(x + 1, M + 1):
        ey, ex = vertices[y]
        if cost[ey][ex] != -1:
            GRAPH.append((cost[ey][ex], x, y))
        
GRAPH.sort(key = lambda x: x[0])
        
parent = [ x for x in range(M + 1) ]

def find(a):
    global parent
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]
    
def merge(a, b):
    global parent
    a = find(a)
    b = find(b)
    
    if a == b:
        return False

    parent[a] = b
    return True

answer = 0
count = 0
for cost, x, y in GRAPH:
    if merge(x, y):
        answer += cost
        count += 1

if count == M:
    print(answer)
else:
    print(-1)