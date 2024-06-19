n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append(a-b)
arr.sort()

print(1 if n & 1 else arr[n//2]-arr[n//2-1]+1)