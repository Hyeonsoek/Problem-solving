from itertools import product

a, b = map(int, input().split())

result = []
for x in range(1, 10):
    for pd in product(['4', '7'], repeat=x):
        value = int(''.join(pd))
        if a <= value <= b:
            result.append(value)

print(len(result))