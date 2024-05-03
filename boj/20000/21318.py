import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
prefix = [0] * n

for x in range(1, n):
    prefix[x] = 1 if arr[x] < arr[x-1] else 0
    prefix[x] += prefix[x-1]

qn = int(input())
result = []
for _ in range(qn):
    s, e = map(int, input().split())
    result.append(prefix[e-1]-prefix[s-1])

print(*result, sep='\n')