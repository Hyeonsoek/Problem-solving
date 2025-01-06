n = int(input())

maxResult = n * (n - 1) // 2

start = 3
maxValues = [1, 2]
minusValues = set([-1])
while len(minusValues) < maxResult:
    for x in maxValues:
        if x - start in minusValues:
            break
    else:
        maxValues.append(start)
        for x in maxValues:
            minusValues.add(x - start)
    
    start += 1


minResult = n - 1
minValues = list(range(1, n + 1))

print(maxResult)
print(*maxValues)
print(minResult)
print(*minValues)