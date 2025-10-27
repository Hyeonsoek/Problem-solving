import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    m = int(input())
    
    cache = [0] * (m + 1)
    cache[0] = 1
    
    for i in range(n):
        for j in range(1, m + 1):
            if j - arr[i] >= 0:
                cache[j] += cache[j - arr[i]]
    
    print(cache[m])

for _ in range(int(input())):
    solve()