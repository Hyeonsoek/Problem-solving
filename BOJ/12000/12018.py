import sys
input = sys.stdin.readline

n, m = map(int, input().split())

target = []
for _ in range(n):
    p, l = map(int, input().split())
    arr = sorted(list(map(int, input().split())), reverse=True)
    target.append(arr[l-1] if p >= l else 1)

target.sort()
result = 0
for x in range(n):
    if m >= target[x]:
        m -= target[x]
        result += 1

print(result)