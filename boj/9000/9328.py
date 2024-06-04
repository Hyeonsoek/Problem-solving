import sys
from collections import deque
input = sys.stdin.readline
dirr = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def solve():
    H, W = map(int, input().split())
    board = [['.'] * (W + 2) for _ in range(H + 2)]
    
    for x in range(1, H + 1):
        line = input().strip()
        for y in range(1, W + 1):
            board[x][y] = line[y-1]
    
    keys = set(input().strip())
    document = set()
    
    documentSize, keySize = 0, len(keys)
    
    while True:
        queue = deque([(0, 0)])
        visited = [[0] * (W+2) for _ in range(H+2)]
        visited[0][0] = 1
        
        while queue:
            y, x = queue.popleft()
            
            for ydir, xdir in dirr:
                yy = y + ydir
                xx = x + xdir
                if 0 <= yy < H+2 and 0 <= xx < W+2 \
                    and board[yy][xx] != '*' and not visited[yy][xx]:
                
                    if 'A' <= board[yy][xx] <= 'Z' \
                            and board[yy][xx].lower() in keys:
                        visited[yy][xx] = 1
                        queue.append((yy, xx))
                        
                    if 'a' <= board[yy][xx] <= 'z':
                        visited[yy][xx] = 1
                        queue.append((yy, xx))
                        keys.add(board[yy][xx])
                    
                    if board[yy][xx] == '.':
                        visited[yy][xx] = 1
                        queue.append((yy, xx))
                        
                    if board[yy][xx] == '$':
                        visited[yy][xx] = 1
                        queue.append((yy, xx))
                        document.add((yy, xx))
        
        if keySize == len(keys) and documentSize == len(document):
            break
        
        keySize = len(keys)
        documentSize = len(document)
            
    return len(document)

T = int(input())
for a in range(T):
    print(solve())