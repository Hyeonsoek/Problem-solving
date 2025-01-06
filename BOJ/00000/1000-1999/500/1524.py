t = int(input())
for _ in range(t):
    input()
    n, m = map(int, input().split())
    aarr = sorted(list(map(int, input().split())))
    barr = sorted(list(map(int, input().split())))
    
    a = b = 0
    while a < n and b < m:
        if aarr[a] < barr[b]:
            a += 1
        else:
            b += 1
    
    if a == n:
        print("B")
    elif b == m:
        print("S")