import sys

n, k = map(int, input().split())
array = sorted([int(sys.stdin.readline()) for _ in range(n)])

low, high = 1, array[-1] - array[0]
answer = 1

while low <= high:
    mid = (low + high) // 2
    count = 1
    last = array[0]
    
    for x in array[1:]:
        if x - last >= mid:
            count += 1
            last = x
    
    if count >= k:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1
        
print(answer)