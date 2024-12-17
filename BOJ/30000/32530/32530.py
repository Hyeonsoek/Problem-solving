import sys
input = sys.stdin.readline

def after10(hh, mm):
    return hh + (mm + 10) // 60, (mm + 10) % 60

def solve():
    n = int(input())
    arr = sorted([tuple(map(int, input().split(':'))) for _ in range(n)])
    visited = [0] * n
    
    count = 0
    for x in range(n):
        if visited[x]:
            continue
        
        time = after10(*arr[x])
        for i in range(x, x + 3):
            if i < n and time >= arr[i]:
                visited[i] = 1
        
        count += 1
    
    print(count)

solve()