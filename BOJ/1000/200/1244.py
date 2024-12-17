n = int(input())
arr = [0, *map(int, input().split())]
m = int(input())

for _ in range(m):
    q, index = map(int, input().split())
    
    if q & 1:
        for x in range(index, n + 1, index):
            arr[x] ^= 1
    else:
        left, right = index, index
        while left >= 1 and right <= n and arr[left] == arr[right]:
            left -= 1
            right += 1
        
        for x in range(left + 1, right):
            arr[x] ^= 1

for x in range(1, n + 1, 20):
    print(*arr[x:x+20])