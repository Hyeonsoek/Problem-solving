import sys, collections
input = sys.stdin.readline

n, m = int(input()), int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
bgraph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, time = map(int, input().split())
    
    indegree[end] += 1
    graph[start].append((end, time))
    bgraph[end].append((start, time))

def find_critical(start, end):
    times = [0 for _ in range(n + 1)]
    
    queue = collections.deque()
    queue.append(start)
    
    for x in range(1, n + 1):
        if queue:
            vertex = queue.popleft()
            cur_time = times[vertex]
            
            for next, next_time in graph[vertex]:
                indegree[next] -= 1
                times[next] = max(times[next], cur_time + next_time)
                if not indegree[next]:
                    queue.append(next)
    
    queue.clear()
    queue.append(end)
    
    visited = [0] * (n + 1)
    visited[end] = 1
    
    result = 0
    
    while queue:
        vertex = queue.popleft()
        
        for next, next_time in bgraph[vertex]:
            if times[vertex] - times[next] == next_time:
                result += 1
                if not visited[next]:
                    visited[next] = 1
                    queue.append(next)

    return times[end], result

qstart, qend = map(int, input().split())
print(*find_critical(qstart, qend), sep='\n')