import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
strings = [list(input().rstrip()) for _ in range(n)]

keys = set()
for string in strings:
    for char in string:
        keys.add(char)

indegree = defaultdict(int)
graph = defaultdict(set)

for a in range(n - 1):
    for b in range(a + 1, n):
        string_a = strings[a]
        string_b = strings[b]
        count = min(len(string_a), len(string_b))
        
        for index in range(count):
            start = string_a[index]
            end = string_b[index]
            
            if start != end:
                if end not in graph[start]:
                    graph[start].add(end)
                    indegree[end] += 1
                break
        
            if index == count - 1 and len(string_a) > len(string_b):
                print("!")
                exit(0)

queue = deque()
for key in keys:
    if not indegree[key]:
        queue.append(key)
        
result = []
for x in range(len(keys)):
    if queue:
        if len(queue) >= 2:
            print("?")
            exit(0)
        
        vertex = queue.popleft()
        result.append(vertex)
        
        for next in graph[vertex]:
            indegree[next] -= 1
            if not indegree[next]:
                queue.append(next)
    else:
        print("!")
        exit(0)

print(''.join(result))