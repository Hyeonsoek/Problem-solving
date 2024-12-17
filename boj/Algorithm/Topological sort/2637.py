import sys, collections
input = sys.stdin.readline

n, m = int(input()), int(input())
indegree = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]

for x in range(m):
    end, start, count = map(int, input().split())
    
    adj[start].append((end, count))
    indegree[end] += 1
    
counts = [ collections.defaultdict(int) for _ in range(n + 1) ]
queue = collections.deque()
for x in range(1, n + 1):
    if not indegree[x]:
        queue.append(x)
        counts[x][x] = 1

for _ in range(n):
    if queue:
        vertex = queue.popleft()
        
        for next, count in adj[vertex]:
            indegree[next] -= 1
            for vv, cc in counts[vertex].items():
                counts[next][vv] += cc * count
                
            if not indegree[next]:
                queue.append(next)

for x in sorted(counts[n].items()):
    print(*x)

# print(counts[n].items())