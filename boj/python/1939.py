from sys import stdin
from collections import defaultdict, deque
input = stdin.readline

n, m = map(int, input().split())

directions = defaultdict(list)
for x in range(m):
    a, b, c = map(int, input().split())
    
    directions[a].append((b, c))
    directions[b].append((a, c))
    
start, end = map(int, input().split())
    
def bfs(weight):
    queue = deque()
    visited = [False] * (n + 1)
    
    queue.append(start)
    visited[start] = True
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            return True
        
        for next, next_weight in directions[current]:
            if visited[next] == False and next_weight >= weight:
                queue.append(next)
                visited[next] = True
    
    return False

low, high = 1, 10 ** 9
while low <= high:
    mid = (low + high) // 2
    
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1

print(high)