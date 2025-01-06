n = int(input())
arr = [1, 0, 0]

for _ in range(n):
    a, b = map(int, input().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
    
for x in range(3):
    if arr[x]:
        print(x+1)