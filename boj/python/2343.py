n, m = map(int, input().split())
lectures = list(map(int, input().split()))

low, high = 1, 10 ** 9

while low <= high:
    mid = (low + high) // 2
    
    count, temp = 0, 0
    for x in lectures:
        if x > mid:
            count = 10 ** 9
            break
        
        if temp + x <= mid:
            temp += x
        else:
            temp = x
            count += 1
    
    if count >= m:
        low = mid + 1
    else:
        high = mid - 1
        
print(low)