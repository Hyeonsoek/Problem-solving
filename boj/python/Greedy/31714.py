import sys
input = sys.stdin.readline

def solve():
    n, m, d = map(int, input().split()) 
    arr = [[] for _ in range(n)]
    for x in range(n):
        for y in list(map(int, input().split())):
            arr[x].append((y + x * d, x))
        arr[x].sort()
    
    arr = list(zip(*arr))
    answer = tuple(range(n))

    for x in range(m):
        arr[x] = sorted(arr[x], key=lambda v: (v[0], -v[1]))
        
        if list(zip(*arr[x]))[1] != answer:
            return "NO"
    return "YES"

print(solve())