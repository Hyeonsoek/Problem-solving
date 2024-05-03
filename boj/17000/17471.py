import random
from itertools import combinations
from collections import deque

def bfs(group : set) -> bool:
    check = [False for x in range(N+1)]
    queue = deque()
    
    random_value = random.choice(list(group))
    queue.append(random_value)
    check[random_value] = True
    
    while queue:
        current = queue.popleft()
        
        for x in graph[current]:
            if x in group and check[x] == False:
                check[x] = True
                queue.append(x)
    
    for x in group:
        if check[x] == False:
            return False
    
    return True

N = int(input())
population = list(map(int, input().split()))

graph = [set() for x in range(N + 1)]

for start in range(1, N+1):
    numbers = list(map(int, input().split()))
    
    if numbers[0] == 0:
        continue
    
    ends = numbers[1:]
    
    for end in ends:
        if start != end:
            graph[start].add(end)
            graph[end].add(start)

MAX = 987654321
answer = MAX

for count in range(1, N):
    for group_a in combinations(range(1, N+1), count):
        group_b = set(range(1, N+1)) - set(group_a)
        
        validate_a = bfs(group_a)
        validate_b = bfs(group_b)
        
        if validate_a and validate_b:
            popul_a = sum([population[x - 1] for x in group_a])
            popul_b = sum([population[x - 1] for x in group_b])
            answer = min(answer, abs(popul_a - popul_b))
            
print(answer if answer != MAX else -1)