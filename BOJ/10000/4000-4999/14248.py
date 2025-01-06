import collections

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

visited = [0] * (n + 1)
visited[s] = 1

queue = collections.deque([s])
while queue:
    cur = queue.popleft()
    
    for dx in [-arr[cur-1], arr[cur-1]]:
        xx = cur + dx
        if 1 <= xx <= n and not visited[xx]:
            visited[xx] = 1
            queue.append(xx)
            
print(sum(visited))