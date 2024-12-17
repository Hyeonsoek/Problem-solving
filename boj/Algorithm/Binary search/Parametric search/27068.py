from sys import stdin
from collections import deque
input = stdin.readline
dirr = [[-1, 0], [1, 0], [0, 1], [0, -1]]

N, M, K, X = map(int, input().split())
image = [ list(map(int, input().split())) for _ in range(N) ]
            
def count(mid : int) -> int:
    result = 0
    check = [ [False for _ in range(M)] for _ in range(N) ]
    
    def bfs(sy, sx) -> int:
        queue = deque()
        queue.append((sy, sx))
        check[sy][sx] = True
        
        count = 1
        while queue:
            y, x = queue.popleft()
            
            for ydir, xdir in dirr:
                yy, xx = y + ydir, x + xdir
                if 0 <= yy < N and 0 <= xx < M and not check[yy][xx]:
                    if X - image[yy][xx] > mid:
                        check[yy][xx] = True
                        queue.append((yy, xx))
                        count += 1
        
        return count
      
    for y in range(N):
        for x in range(M):
            if X - image[y][x] <= mid or check[y][x]:
                continue

            for ydir, xdir in dirr:
                yy, xx = y + ydir, x + xdir
                if 0 <= yy < N and 0 <= xx < M and not check[yy][xx]:
                    if abs(image[yy][xx] - image[y][x]) > mid:
                        result += bfs(y, x)
                        break
                    
    return result
                
low, high = 0, X 
while low <= high:
    mid = (low + high) // 2
    result = count(mid)
    
    if result <= K:
        high = mid - 1
    else:
        low = mid + 1
        
print(low)