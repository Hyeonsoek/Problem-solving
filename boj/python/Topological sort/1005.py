import sys, collections
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    
    indegree = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(k):
        start, end = map(int, input().split())
        adj[start].append(end)
        indegree[end] += 1

    result = [0] * (n + 1)
    queue = collections.deque()
    for x in range(1, n + 1):
        if not indegree[x]:
            queue.append(x)
            result[x] = time[x]

    for x in range(1, n + 1):
        if queue:
            vertex = queue.popleft()
            
            for next in adj[vertex]:
                result[next] = max(result[next], result[vertex] + time[next])
                
                indegree[next] -= 1
                if not indegree[next]:
                    queue.append(next)
    
    print(result[int(input())])