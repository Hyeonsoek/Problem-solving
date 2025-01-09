n, r = map(int, input().split())

result = set()
target = n - r
for x in range(1, int(target ** .5) + 1):
    if target % x == 0:
        if x > r:
            result.add(x)
        if target // x > r:
            result.add(target // x)
            
print(sum(result))