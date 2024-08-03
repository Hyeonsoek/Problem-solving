import itertools

n = int(input())
arr = []
for x in range(1, 7):
    for perm in itertools.product(['4', '7'], repeat=x):
        arr.append(int(''.join(perm)))
arr.sort()

result = 0
for x in arr:
    if x <= n:
        result = x

print(result)