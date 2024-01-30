import sys, collections
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    indegree = [0] * (n + 1)
    team = list(map(int, input().split()))
    graph = [set() for _ in range(n + 1)]
    
    for rank_x in range(n - 1):
        for rank_y in range(rank_x + 1, n):
            graph[team[rank_x]].add(team[rank_y])
            indegree[team[rank_y]] += 1
    
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if b in graph[a]:
            a, b = b ,a
            
        graph[b].remove(a)
        graph[a].add(b)
        indegree[a] -= 1
        indegree[b] += 1
    
    result = [0] * n
    queue =  collections.deque()
    for x in range(1, n + 1):
        if not indegree[x]:
            queue.append(x)

    check = True
    for x in range(n):
        if queue:
            if len(queue) >= 2:
                check = False
                print("?")
                break
            
            vertex = queue.popleft()
            result[x] = vertex
            
            for next in graph[vertex]:
                indegree[next] -= 1
                if not indegree[next]:
                    queue.append(next)
        else:
            check = False
            print("IMPOSSIBLE")
            break
    
    if check:
        print(*result)