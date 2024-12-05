import sys
input = sys.stdin.readline

def solve():
    n, m, d, l = map(int, input().split())
    arr = sorted([int(input()) for _ in range(n)], reverse=True)
    
    result = [[] for _ in range(m)]
    
    while arr and arr[-1] < l:
        arr.pop()
    
    for i in range(m):
        if arr:
            result[i].append(arr.pop())
    
    floor = 1
    while arr:
        speed = floor * d
        for i in range(m):
            while arr and arr[-1] - speed < l:
                arr.pop()
            if arr:
                result[i].append(arr.pop())
        floor += 1
    
    print(sum(map(len, result)))

solve()