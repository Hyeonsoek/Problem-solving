import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)])

result = 0
for x in range(n):
    result += abs(x + 1 - arr[x])
    
print(result)