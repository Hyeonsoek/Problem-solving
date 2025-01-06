n = int(input())
arr = list(map(int, input().split()))

result = [0] * n
targets = list(range(n))

for x in range(n):
    result[targets[arr[x]]] = x + 1
    del targets[arr[x]]
    
print(*result)