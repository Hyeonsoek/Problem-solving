K = int(input())

numbers = [ 1 ] * 131

for x in range(130):
    numbers[x + 1] = numbers[x] + (x + 2)

for x in range(1, 131):
	numbers[x] += numbers[x-1]

cache = [ x for x in range(K + 1) ]

for x in range(1, K + 1):
    for y in range(131):
        if x - numbers[y] < 0:
            break
        
        if cache[x] > cache[x - numbers[y]] + 1:
            cache[x] = cache[x - numbers[y]] + 1

print(cache[K])