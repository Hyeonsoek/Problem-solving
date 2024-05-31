a, b, c = map(int, input().split())
arr = [0] * (a * b * c + 1)

for x in range(1, a + 1):
    for y in range(1, b + 1):
        for z in range(1, c + 1):
            arr[x + y + z] += 1
            
print(arr.index(max(arr)))