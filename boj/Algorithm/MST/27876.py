import math, sys
sys.setrecursionlimit(100000000)

n = int(input())

target = int(math.sqrt(2 * n - 1))
squares = [ x * x for x in range(2, target + 1) ]
parent = [ x for x in range(n + 1) ]

def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u, v):
    u = find(u)
    v = find(v)
    
    if u == v:
        return False
    
    parent[u] = v
    return True

array = []

answer, count = 1, 0
for distance in range(1, n):
    is_odd = distance & 1
    _start = 1 if is_odd else 0
    for index in range(_start, target - 1, 2):
        square, start, end = squares[index], 0, 0
        if is_odd:
            start = square // 2 + (distance // 2 + 1)
            end = square // 2 - (distance // 2)
        else:
            start = square // 2 + (distance // 2)
            end = square // 2 - (distance // 2)    
            
        if 1 <= start <= n and 1 <= end <= n and start != end and merge(start, end):
            array.append((start, end, distance))
            answer *= distance
            answer %= 998244353
            count += 1
            
            if count == n - 1:
                for xxx in array:
                    print(xxx)
                print(answer)
                exit(0)

print(-1)