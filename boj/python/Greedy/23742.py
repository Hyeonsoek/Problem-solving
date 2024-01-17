n = int(input())
array = sorted(list(map(int, input().split())))

last = -1
ps, ns = 0, 0
for x in range(n):
    if array[x] >= 0:
        ps += array[x]
    else:
        ns += array[x]
        last = x

current = ps * (n - (last + 1)) + ns
for x in range(last, -1, -1):
    ps += array[x]
    ns -= array[x]
    
    current = max(ps * (n - x) + ns, current)

print(current)