import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [ x for x in range(n + 1) ]

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def merge(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return
    
    parent[a] = b

for _ in range(m):
    command, a, b = map(int, input().split())
    
    if command == 0:
        merge(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")