from itertools import combinations

n, m = map(int, input().split())
array = list(map(int, input().split()))

result = 300000
for x in combinations(array, 3):
    s = sum(x)
    if s <= m:
        result = min(result, m - s)
print(m - result)