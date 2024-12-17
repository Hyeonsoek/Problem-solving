import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

MAX_DEPTH = 17

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    input_a, input_b, cost = map(int, input().split())
    
    graph[input_a].append((input_b, cost))
    graph[input_b].append((input_a, cost))
    
parent = [ [0] * MAX_DEPTH for _ in range(n + 1) ]
distance = [ [0] * MAX_DEPTH for _ in range(n + 1) ]
depth = [ 0 ] * (n + 1)

def dfs(node):
    for next, cost in graph[node]:
        if not depth[next]:
            depth[next] = depth[node] + 1
            parent[next][0] = node
            distance[next][0] = cost
            dfs(next)

depth[1] = 1
dfs(1)

for pow in range(1, MAX_DEPTH):
    for node in range(1, n + 1):
        prev = parent[node][pow - 1]
        if prev == 0:
            continue
        parent[node][pow] = parent[ prev ][pow - 1]
        distance[node][pow] = distance[node][pow - 1] + distance[ prev ][pow - 1]

m = int(input())
for _ in range(m):
    query = list(map(int, input().split()))
    
    flag = True
    q, input_a, input_b = query[0], query[1], query[2]
    a, b = input_a, input_b
    
    if depth[a] < depth[b]:
        a, b = b, a
        flag = False
        
    cost, length_a, length_b = 0, 1, 1
    for pow in range(MAX_DEPTH - 1, -1, -1):
        if depth[a] - depth[b] >= 2 ** pow:
            length_a += 2 ** pow
            cost += distance[a][pow]
            a = parent[a][pow]
    
    if a != b:
        for pow in range(MAX_DEPTH - 1, -1, -1):
            if parent[a][pow] and parent[a][pow] != parent[b][pow]:
                cost += (distance[a][pow] + distance[b][pow])
                length_a += 2 ** pow
                length_b += 2 ** pow
                a = parent[a][pow]
                b = parent[b][pow]
        
        cost += (distance[a][0] + distance[b][0])
        length_a += 1
        length_b += 1
    
    if q == 1:
        print(cost)
    else:
        index = query[3]
        start = input_a
        target = index - 1
        
        if index > (length_a if flag else length_b):
            start = input_b
            target = length_a + length_b - index - 1
            
        for pow in range(MAX_DEPTH - 1, -1, -1):
            if parent[start][pow] and target >= 2 ** pow:
                target -= 2 ** pow
                start = parent[start][pow]
            
            if target == 0:
                print(start)
                break

# 12
# 1 2 1
# 2 4 1
# 2 5 2
# 1 3 1
# 3 6 2
# 6 7 1
# 6 8 1
# 5 9 1
# 5 10 1
# 4 11 1
# 4 12 1
# 2
# 2 2 7 5
# 2 12 6 5

# 6
# 1 2 1
# 2 4 1
# 2 5 2
# 1 3 1
# 3 6 2
# 0