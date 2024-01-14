from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
ranges = sorted([ list(map(int, input().split())) for _ in range(m) ])

low, high = 1, 10 ** 18
while low <= high:
    mid = (low + high) // 2
    
    count = 1
    location = ranges[0][0]
    for index in range(m):
        start, end = ranges[index]
        while location + mid <= end:
            count += 1
            location = max(location + mid, start)
            
    if count < n:
        high = mid - 1
    else:
        low = mid + 1
        
print(high)