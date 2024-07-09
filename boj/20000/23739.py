n = int(input())
arr = [int(input()) for _ in range(n)]

x = 0
result = 0
while x < n:
    time = 0
    while x < n and time + arr[x] <= 30:
        time += arr[x]
        result += 1
        x += 1
    
    if x < n:
        if 30 - time >= arr[x] / 2:
            result += 1
        
        if time < 30:
            x += 1

print(result)