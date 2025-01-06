import sys

n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(m)], reverse=True)

price = sys.maxsize
result = 0
for x in range(min(n, m)):
    if price > arr[x] and arr[x] * (x + 1) >= result:
        price = arr[x]
        result = arr[x] * (x + 1)

print(price, result, sep='\n')