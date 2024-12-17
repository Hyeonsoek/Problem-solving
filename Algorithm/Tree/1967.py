import sys
from collections import defaultdict
sys.setrecursionlimit(20000)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
lengths = [defaultdict(int) for x in range(n + 1)]

for _ in range(n - 1):
    parent, child, cost = map(int, input().split())
    tree[parent].append((child, cost))

def diameter(x):
    result = 0
    costs = []
    
    for child, _ in tree[x]:
        result = max(result, diameter(child))
        costs.append(lengths[x][child])
    
    result = max(result, sum(sorted(costs)[-2:]))
    return result

def max_length(x):
    result = 0
    
    for child, cost in tree[x]:
        next_cost = max_length(child) + cost
        lengths[x][child] = max(next_cost, lengths[x][child])
        result = max(next_cost, result)
        
    return result

max_length(1)
print(diameter(1))

# for x in range(1, n + 1):
#     print(x, *lengths[x].items())