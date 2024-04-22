n = int(input())
graph = [list(map(lambda x: 1 if x == 'Y' else 0, input())) for _ in range(n)]

count = [0] * n
for a in range(n):
    for b in range(n):
        if a == b:
            continue
        
        if graph[a][b]:
            count[a] += 1
            continue
        
        for c in range(n):
            if graph[a][c] and graph[b][c]:
                count[a] += 1
                break

print(max(count))