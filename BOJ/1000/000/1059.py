l = int(input())
arr = sorted(list(map(int, input().split())) + [0, 1001])
n = int(input())

result = []
for x in range(l + 1):
    for a in range(arr[x]+1, arr[x+1]-1):
        for b in range(a + 1, arr[x+1]):
            if a <= n <= b:
                result.append((a, b))

print(len(result))