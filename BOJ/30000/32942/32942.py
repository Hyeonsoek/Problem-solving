A, B, C = map(int, input().split())

graph = [set() for _ in range(11)]

for i in range(1, 11):
    for j in range(1, 11):
        if A * i + B * j == C:
            graph[i].add(j)

for i in range(1, 11):
    if graph[i]:
        print(*sorted(graph[i]))
    else:
        print(0)