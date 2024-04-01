n = int(input())
arr = list(map(int, input().split()))

dicts = {}
for x in range(n):
    value = arr[x]
    
    while not (value & 1):
        value //= 2
        
    if value in dicts:
        dicts[value] += 1
    else:
        dicts[value] = 1

print(max(dicts.values()))