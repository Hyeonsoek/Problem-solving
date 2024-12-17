from sys import stdin
input = stdin.readline

d, n, m = map(int, input().split())
locations = [ 0 ] + sorted([ int(input()) for _ in range(n) ]) + [ d ]

answer = 0
low, high = 1, 10 ** 9
while low <= high:
    count, last = 0, 0
    mid = (low + high) // 2
    for x in range(1, n + 2):
        if locations[x] - locations[last] < mid:
            count += 1
        else:
            last = x
            
    if count <= m:
        low = mid + 1
    else:
        high = mid - 1

print(high)