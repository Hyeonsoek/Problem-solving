import sys, collections
input = sys.stdin.readline

n = int(input())
time = [0] * n
indegree = [0] * n
board = [[] for _ in range(n)]

for x in range(n):
    timex, *vertices = map(int, input().split())
    
    time[x] = timex
    for vertex in vertices[:-1]:
        board[vertex - 1].append(x)
        indegree[x] += 1

result = [0] * n
queue = collections.deque()
for x in range(n):
    if not indegree[x]:
        queue.append(x)
        result[x] = time[x]

for x in range(n):
    if queue:
        vertex = queue.popleft()
        
        for next in board[vertex]:
            result[next] = max(result[next], result[vertex] + time[next])
            indegree[next] -= 1
            if not indegree[next]:
                queue.append(next)
                
print(*result, sep='\n')