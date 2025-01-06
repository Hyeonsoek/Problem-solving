n = int(input())
arr = [input() for _ in range(n)]

index = 0
result = len(arr[0])
while True:
    s = set()
    for x in range(n):
        s.add(arr[x][index:])
    
    if len(s) == n:
        result = len(s.pop())
        index += 1
    else:
        break

print(result)