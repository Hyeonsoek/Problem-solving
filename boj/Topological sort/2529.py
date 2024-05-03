import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
string = list(input().strip().split())

indegree = [0] * (n + 2)
graph = [[] for _ in range(n + 2)]

for index, char in enumerate(string):
    start, end = index + 2, index + 1
    if char == '>':
        start, end = end, start
    
    graph[start].append(end)
    indegree[end] += 1

def find_value(indegree, start, reverse = False):
    queue = PriorityQueue()
    result = [0] * (n + 2)
    
    for x in range(1, n + 2):
        if not indegree[x]:
            queue.put(-x if reverse else x)
    
    for x in range(1, n + 2):
        if not queue.empty():
            vertex = queue.get() * (-1 if reverse else 1)
            
            result[vertex] = start
            start -= 1
            
            for next in graph[vertex]:
                indegree[next] -= 1
                if not indegree[next]:
                    queue.put(-next if reverse else next)
    
    return "".join(map(str, result[1:]))

print(find_value(indegree[:], 9))
print(find_value(indegree[:], n, True))