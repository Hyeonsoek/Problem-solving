from sys import stdin
from collections import deque
input = stdin.readline
dirr = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            
def count(mid, n, m, X, image):
    result = 0
    isVisited = [ [False for _ in range(m)] for _ in range(n) ]
    
    def bfs(sx, sy):
        queue = deque([(sy, sx)])
        isVisited[sy][sx] = True
        
        count = 1
        while queue:
            y, x = queue.popleft()
            
            for ydir, xdir in dirr:
                yy, xx = y + ydir, x + xdir
                if 0 <= yy < n and 0 <= xx < m and not isVisited[yy][xx]:
                    if X - image[yy][xx] > mid:
                        isVisited[yy][xx] = True
                        queue.append((yy, xx))
                        count += 1
        return count
      
    for y in range(n):
        for x in range(m):
            if X - image[y][x] <= mid or isVisited[y][x]:
                continue

            for ydir, xdir in dirr:
                yy, xx = y + ydir, x + xdir
                if 0 <= yy < n and 0 <= xx < m and not isVisited[yy][xx]:
                    if abs(image[yy][xx] - image[y][x]) > mid:
                        result += bfs(x, y)
                        break
                    
    return result
                
def solve():
    n, m, k, x = map(int, input().split())
    image = [ list(map(int, input().split())) for _ in range(n) ]
    
    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        result = count(mid, n, m, x, image)
        
        if result <= k:
            high = mid - 1
        else:
            low = mid + 1
            
    print(low)

solve()