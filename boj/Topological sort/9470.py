import sys, collections
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    k, m, p = map(int, input().split())
    adj = [[] for _ in range(m + 1)]
    indegree = [0] * (m + 1)
    
    for _ in range(p):
        start, end = map(int, input().split())
        adj[start].append(end)
        indegree[end] += 1
        
    result = [1] * (m + 1)
    dicts = [ collections.defaultdict(int) for _ in range(m + 1) ]
    queue = collections.deque()
    for x in range(1, m + 1):
        if not indegree[x]:
            queue.append(x)
    
    for x in range(1, m + 1):
        if queue:
            vertex = queue.popleft()
            
            for key, value in dicts[vertex].items():
                next = key + (1 if value >=2 else 0)
                result[vertex] = max(result[vertex], next)
                
            for next in adj[vertex]:
                indegree[next] -= 1
                dicts[next][result[vertex]] += 1
                if not indegree[next]:
                    queue.append(next)
                    
    print(k, max(result))